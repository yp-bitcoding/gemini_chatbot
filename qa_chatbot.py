from dotenv import load_dotenv
import time
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    """Fetch response from Gemini AI."""
    start_time = time.perf_counter()
    response = chat.send_message(question, stream=True)
    print(f"End : {time.perf_counter() - start_time}")
    return response


# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize the session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

if submit and user_input:
    response = get_gemini_response(user_input)

    # Add user query and response to session chat history
    st.session_state["chat_history"].append(("You", user_input))
    
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot", chunk.text))