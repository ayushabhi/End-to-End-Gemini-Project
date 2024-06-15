import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title = "Gemini - Image to Text")
st.header("Gemini Application")
input = st.text_input("Input Prompt: ",key = "input")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "uploaded image", use_column_width = True)

submit = st.button("Generate")

#if submit is clicked
if submit:
    response = get_response(input,image)
    st.subheader("The response is ")
    st.write(response)