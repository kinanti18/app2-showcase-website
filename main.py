import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=600)

with col2:
    st.title("Kinan")
    content = """
    Hi, Welcome to Kinan's Digital Curriculum Vitae. 
    Kinan is a Fresh Graduate of Informatics with passion in technology, 
    especially for Python Programming, Java, R, Web Design, SQL, Data Science, 
    AI/ML, Computer Vision & Deep Learning. She loves writing, painting, reading books,
    and also listen to the music to spend her spare time. 
    And feel happy because those stuff can reach by  'technology'. 
    By working in the Technology Industry, she always tries to find out of the box idea. 
    Currently, she's working on her portfolio. 
    Also, she's still and counting to make a new journey 
    and to be a better Kinan each day."""
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)