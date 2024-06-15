import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#fun to load the model and get the response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question,stream=True)
    return response

#initialze the stramlit app
st.set_page_config(page_title = "Q & A Chat")
st.subheader("Gemini LLM Application")

#initialize the session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input = st.text_input("Input: ",key = 'input')
submit = st.button("Ask the question")

if submit and input:
    response = get_response(input)
    #Add the quesry and response to session chat history
    st.session_state['chat_history'].append(("you",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot",chunk.text))

st.subheader("The Chat History is")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")