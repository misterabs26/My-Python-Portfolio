import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address: ",
                               key="email")
    user_message = st.text_area("Your message here:",
                                key="message")
    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        print("I was pressed!")

    st.session_state

