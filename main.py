import streamlit as st
import google.generativeai as genai
import time
import random
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the .env file
gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

st.set_page_config(
    page_title="Text Emotion Analysis with Gemini Pro",
    page_icon=""
)

st.title("Text Emotion Analysis with Gemini Pro")
st.caption("Text Emotion Analysis with Gemini Pro")

# Initialize history if not already present in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Only configure the API if the key is found
if gemini_api_key:
    try:
        # Configure the Gemini API with the key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=st.session_state.history)
    except Exception as e:
        st.error(f"Failed to configure Gemini Pro API: {e}")
else:
    st.error("Gemini API key is missing in the .env file.")

with st.sidebar:
    if st.button("Clear Chat Window", use_container_width=True, type="primary"):
        st.session_state.history = []
        st.rerun()

# Display the chat history
for message in chat.history:
    role = "assistant" if message.role == 'model' else message.role
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Define possible emotions for the analysis
emotions = [
    'Surprise', 'Fear', 'Sadness', 'Anger', 'Happiness', 'Trust', 'Confusion',
    'Agreement', 'Boredom', 'Guilt', 'Contentment', 'Inquiry', 'Love',
    'Curiosity', 'Anticipation', 'Shame'
]

# Input box for the sentence to analyze
input_sentence = st.text_input("Enter a sentence to analyze:")
if input_sentence and gemini_api_key:
    prompt = f"""
        Analyze the following sentence and provide:
        - Emotion conveyed (choose from: {', '.join(emotions)})
        - Fillers present
        - Grammar mistakes and corrected version
        - Formality of the sentence and a more formal version if informal
        Sentence: {input_sentence}
    """
    with st.chat_message("user"):
        st.markdown(input_sentence)  # Display the input sentence without the question
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        try:
            full_response = ""
            for chunk in chat.send_message(prompt, stream=True):
                word_count = 0
                random_int = random.randint(5, 10)
                for word in chunk.text:
                    full_response += word
                    word_count += 1
                    if word_count == random_int:
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "_")
                        word_count = 0
                        random_int = random.randint(5, 10)
            message_placeholder.markdown(full_response)
        except genai.types.generation_types.BlockedPromptException as e:
            st.exception(e)
        except Exception as e:
            st.exception(e)
        st.session_state.history = chat.history