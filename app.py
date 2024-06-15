from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

#loading all the environment variables
load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
#funtion to load gemini ai model and get the responses
def get_response(question):
    response = model.generate_content(question)
    return response.text

#initialize streamlit app

st.set_page_config(page_title = "Q&A")
st.header("Gemini LLM Application")
input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

#when submit is clicked
if submit:
    response = get_response(input)
    st.subheader("The response is")
    st.write(response)