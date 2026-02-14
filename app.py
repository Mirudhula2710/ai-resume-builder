import streamlit as st
import requests

st.title("AI Resume Builder")

st.write("Welcome! Please enter your details below:")

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email")
skills = st.text_area("Skills (comma separated)")

if st.button("Generate Resume"):
    # Hugging Face router endpoint
    API_URL = "https://router.huggingface.co"
    headers = {"Authorization": "Bearer hf_pFmqAzrtTgjhWGIdEhDMJGjRuBFcKJZpxmB"}  # <-- use your latest token here

    # Prompt for the model
    prompt = f"Generate a professional resume summary for {name}, email {email}, with skills: {skills}."

    # Make the API request
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "model": "tiiuae/falcon-7b-instruct",
            "inputs": prompt
        }
    )

    # Safely decode the response
    try:
        result = response.json()
    except Exception as e:
        st.error("Failed to decode response: " + str(e))
        result = None

    # Display the output
    st.write("### Resume Summary")

    if result:
        if isinstance(result, list) and "generated_text" in result[0]:
            st.write(result[0]["generated_text"])
        elif isinstance(result, dict) and "generated_text" in result:
            st.write(result["generated_text"])
        elif isinstance(result, dict) and "error" in result:
            st.error("API Error: " + result["error"])
        else:
            st.error("Unexpected response format: " + str(result))
