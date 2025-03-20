import smtplib, ssl
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
import re
import streamlit as st


# Load environment variables from .env file
load_dotenv()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def send_email(sender_email,sender_message):
    admin_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    host = "smtp.gmail.com"
    port = 465
    if validate_email(sender_email):
        # Create email with MIMEText
        subject = f"New Message from your portfolio"
        body = f"""
        {sender_email} sent you a message:
        
        {sender_message}
        """
        msg = MIMEText(body)
        msg["From"] = admin_email
        msg["To"] = admin_email
        msg["Subject"] = subject
        msg["Reply-To"] = sender_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(admin_email, password)
            server.sendmail(admin_email, admin_email, msg.as_string())

        st.info("Your email was sent successfully")
    else:
        st.warning("Invalid email")
