import streamlit as st

st.title("AI Resume Builder")

st.write("Welcome! Please enter your details below:")

name = st.text_input("Full Name")
email = st.text_input("Email")
skills = st.text_area("Skills (comma separated)")

if st.button("Generate Resume"):
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Skills:", skills)
