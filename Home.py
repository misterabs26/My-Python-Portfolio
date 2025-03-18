import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
profile_section = st.container()
with st.container():
    content = """ This portfolio is a reflection of my learning process, showcasing the projects I’ve worked on and the skills I’ve gained along the way. 
    I’m always open to collaboration, feedback, and new opportunities, so feel free to reach out!"""
    st.write(content)
project_section = st.container()

with profile_section:
    about_me = """
    Hi! I’m Gerald from the Philippines, an aspiring Python developer with a strong passion for data analysis and web development.
    I’m currently on an exciting journey of learning and building projects to sharpen my skills in Python and other technologies that bring ideas to life.

    My goal is to develop efficient, scalable, and impactful solutions—whether that means automating processes with Python, 
    analyzing data to uncover meaningful insights, or creating dynamic web applications. I enjoy problem-solving and constantly challenging myself with new concepts, as I believe continuous learning is key to growth in the tech industry.
    
    As I progress in my journey, I’m exploring frameworks, libraries, and tools that enhance my development skills. 
    I’m particularly interested in data visualization, backend development, and front-end technologies that help create seamless user experiences.
    """
    st.header("About Me")
    col1,col2 = st.columns([1.5,5])
    with col1:
        st.image("images/photo.jpg", use_container_width=True)
        with st.expander("Socials"):
            st.link_button("Facebook", "https://www.facebook.com/ayeras.gerald26", use_container_width=True,
                           icon=":material/thumb_up:")
            st.link_button("Github", "https://github.com/misterabs26", use_container_width=True,
                           icon=":material/rocket_launch:")
            st.link_button("LinkedIn", "https://www.linkedin.com/in/ghyxen/", use_container_width=True,
                           icon=":material/person_check:")
    with col2:
        st.subheader("Gerald Ayeras")
        st.info(about_me)


df = pd.read_csv("data.csv", sep=";")

with project_section:
    st.header("Projects")
    cols = st.columns(2,gap="large")
    for i, row in df.iterrows():
        col = cols[i % 2]
        with col:
            st.subheader(row["title"],divider="rainbow")
            st.image(f"images/{row["image"]}",use_container_width=True)
            st.markdown(f"""
                <p class="project-desc">{row["description"]}</p>
            """, unsafe_allow_html=True)
            with st.expander("Source Code"):
                st.info(row['url'])