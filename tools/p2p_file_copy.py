import os
import math
import hashlib
import paramiko
import time

def calculate_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def split_file(source_path, chunk_size):
    # Calculate the number of chunks required
    file_size = os.path.getsize(source_path)
    num_chunks = math.ceil(file_size / chunk_size)

    # Create a temporary directory for storing the chunks
    temp_dir = f'{source_path}.chunks'
    os.makedirs(temp_dir, exist_ok=True)

    # Open the source file in binary mode for reading
    with open(source_path, 'rb') as infile:
        for i in range(num_chunks):
            # Read a chunk of data
            data = infile.read(chunk_size)

            # Generate the chunk filename
            chunk_filename = os.path.join(temp_dir, f'chunk{i+1}')

            # Write the chunk to a separate file in binary mode
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(data)

def copy_file(source_path, destination_host, destination_username, destination_password, destination_directory, chunk_size, poll_interval=5, max_poll_attempts=60):
    try:
        # Split the source file into chunks
        split_file(source_path, chunk_size)

        # Connect to the destination server using SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(destination_host, username=destination_username, password=destination_password)

        # Create the destination directory if it does not exist
        if destination_directory:
            ssh_client.exec_command(f'mkdir -p {destination_directory}')

        # Send each chunk to the destination server using SCP
        num_chunks = math.ceil(os.path.getsize(source_path) / chunk_size)
        for i in range(1, num_chunks + 1):
            chunk_filename = f'{source_path}.chunks/chunk{i}'
            destination_filename = f'{destination_directory}/chunk{i}'
            ftp_client = ssh_client.open_sftp()
            ftp_client.put(chunk_filename, destination_filename)
            ftp_client.close()

        # Calculate checksums for source and destination files
        source_checksum = calculate_checksum(source_path)
        destination_checksum = ssh_client.exec_command(f'cd {destination_directory} && sha256sum chunk*').read().decode().split()[0]

        # Compare checksums and verify file integrity
        if source_checksum == destination_checksum:
            print("File transfer completed successfully.")
        else:
            raise Exception("File transfer completed with errors. File may be corrupted.")

        # Polling loop to check destination file availability
        poll_attempts = 0
        while poll_attempts < max_poll_attempts:
            # Check if the destination file exists
            _, stdout, _ = ssh_client.exec_command(f'ls {destination_directory}/chunk*')
            if stdout.read().strip():
                print("Destination file is available.")
                break

            poll_attempts += 1
            time.sleep(poll_interval)

        if poll_attempts >= max_poll_attempts:
            print("Destination file is not available within the specified time.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Clean up the temporary files on the source system
        temp_dir = f'{source_path}.chunks'
        if os.path.exists(temp_dir):
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                os.remove(file_path)
            os.rmdir(temp_dir)

    finally:
        # Clean up the temporary files on the source system
        temp_dir = f'{source_path}.chunks'
        if os.path.exists(temp_dir):
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                os.remove(file_path)
            os.rmdir(temp_dir)

        # Close the SSH connection
        ssh_client.close()

# Usage example
source_file = '/path/to/source/file'
destination_host = 'destination_host'
destination_username = 'destination_username'
destination_password = 'destination_password'
destination_directory = '/path/to/destination/directory'  # Set to an empty string if no specific directory is required
chunk_size = 1024 * 1024  # 1MB

copy_file(source_file, destination_host, destination_username, destination_password, destination_directory, chunk_size)
