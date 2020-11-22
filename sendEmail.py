import smtplib
import os
from email.message import EmailMessage

def sendEmail(filename):
    email = os.environ.get('TEST_EMAIL')
    password = os.environ.get('TEST_PASS')

    msg = EmailMessage()
    msg['Subject'] = 'File test send'
    msg['From'] = email
    msg['To'] = 'akapa298@gmail.com'

    with open(filename, 'r') as f:
        content = f.read()
        msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)
