import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address: ")
    user_message = st.text_area("Your message here:")

    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        if user_email and user_message:
            send_email(user_email, user_message)
        else:
            st.warning("Please fill up the form.")


