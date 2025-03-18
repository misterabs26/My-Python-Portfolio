import smtplib, ssl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

user_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

host ="smtp.gmail.com"
port = 465

receiver = "mister.abs26@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Test
Hi, This is only a test
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_email, password)
    server.sendmail(user_email,receiver, message)