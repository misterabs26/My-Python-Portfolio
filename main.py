import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
row1 = st.empty()

with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Gerald Ayeras")
    content ="""
    Hi, I am **Gerald Ayeras** from the Philippines.
    An aspiring python developer, a data analyst, and a web developer.
    """
    st.info(content)

with row1:
    content = """Below, you can find some of the apps I have built in Python.
    Feel free to contact me!"""
    st.write(content)