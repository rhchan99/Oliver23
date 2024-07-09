import subprocess

def is_meld_installed():
    try:
        # Run the "meld --version" command
        result = subprocess.run(["meld", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the return code is 0 (indicating success)
        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        # If "meld" is not found, return False
        return False

# Check if meld is installed
if is_meld_installed():
    print("Meld is installed on the system.")
else:
    print("Meld is not installed on the system.")
