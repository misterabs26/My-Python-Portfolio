import smtplib, ssl
import os
from email.mime.text import MIMEText
import streamlit as st
# from dotenv import load_dotenv
import re

# Load environment variables from .env file
# load_dotenv()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def send_email(sender_email,sender_message):
    # Use this code if you're using .dotenv instead of streamlit secrets
    # admin_email = os.getenv("EMAIL_USER")
    # password = os.getenv("EMAIL_PASS")

    admin_email = st.secrets["email"]["EMAIL_USER"]
    password = st.secrets["email"]["EMAIL_PASS"]

    host = "smtp.gmail.com"
    port = 465

    if validate_email(sender_email):
        # Create email with MIMEText
        subject = f"New Message from your portfolio"
        body = f"""
    g    {sender_email} sent you a message:
        
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

            st.success("Email was sent successfully")
    else:
        st.error("Please input a valid email")
