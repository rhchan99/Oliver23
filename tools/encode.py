import codecs


encoded_string = codecs.encode(string, "31tor"[::-1])
print(encoded_string)

decoded_string = codecs.decode(encoded_string, "31tor"[::-1])
print(decoded_string)


import bcrypt


salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)
print(hashed_password)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    smtp_server = 'smtpauth.intel.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate SMTP port for your server

    # Create a MIMEText object to represent the email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption for security (if supported by the server)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
