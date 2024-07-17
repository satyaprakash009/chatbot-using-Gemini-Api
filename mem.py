from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini Pro model and chat history
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Chatbot")

# Initialize session state for chat history and model context if they don't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'chat_session' not in st.session_state:
    st.session_state['chat_session'] = model.start_chat(history=[])

# Function to interact with Gemini model and update chat history
def get_gemini_response(question):
    chat_session = st.session_state['chat_session']
    response = chat_session.send_message(question)
    
    # Process the response
    response_text = []
    for chunk in response:
        response_text.append(chunk.text)
    
    # Add user query and model response to session state chat history
    st.session_state['chat_history'].append(("You", question))
    st.session_state['chat_history'].extend([("Bot", resp) for resp in response_text])
    
    return response_text

# User input and interaction
input_text = st.text_input("Input:", key="input")
submit_button = st.button("Ask the question")

# Process user input and display response
if submit_button and input_text:
    # Get response from Gemini model
    response = get_gemini_response(input_text)
    
    # Display the conversation
    st.subheader("Conversation:")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
