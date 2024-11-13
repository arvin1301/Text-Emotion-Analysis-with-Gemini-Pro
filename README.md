# Text-Emotion-Analysis-with-Gemini-Pro
This project implements a Text Emotion Analysis tool using the Google Gemini Pro API to analyze the emotional content of input sentences. The application evaluates the following aspects of a given text:

-Emotion conveyed: Detects emotions from a predefined list such as Happiness, Anger, Sadness, etc.
-Fillers present: Identifies filler words in the sentence.
-Grammar mistakes: Highlights grammar issues and provides corrections.
-Formality: Assesses the formality of the sentence and offers a more formal version if necessary.

This tool is built with Streamlit for a user-friendly web interface and uses the Google Gemini Pro API for text analysis.

# Features
-Real-time Emotion Analysis: Detects and categorizes emotions such as fear, happiness, and surprise.
-Grammar and Filler Detection: Identifies fillers and grammar mistakes.
-Formality Analysis: Suggests a more formal version of informal sentences.
-Clear History: Option to clear chat history for a fresh start.


# Prerequisites
To run this project, you need to have the following dependencies installed:
-Python 3.x
-Streamlit
-Google Gemini API
-python-dotenv (for loading environment variables)

# Install dependencies using pip:
pip install streamlit google-generativeai python-dotenv

# Setup
Create a .env file in the root directory with the following content:

GOOGLE_GEMINI_API_KEY=your_api_key
Replace your_api_key with your actual Google Gemini API key.

# Run the Streamlit application:
streamlit run app.py

The application will open in your default web browser, where you can start entering sentences to analyze.

# How to Use
1.Enter a Sentence: Type a sentence in the input box and hit Enter.

2.View Results: The application will display:
-Emotion detected in the sentence
-Filler words (if any)
-Grammar mistakes and corrections
-Formality of the sentence and a formal version if needed

3.Clear History: Click the "Clear Chat Window" button in the sidebar to reset the chat history.

# Notes
-The application uses streaming to display the response progressively as the model generates the output.
-If the Gemini API key is missing or invalid, the application will show an error message.

Screenshot:
![text](https://github.com/user-attachments/assets/591a5cd1-dd08-4acd-8b1d-4c6a932cba9a)
![text emotion](https://github.com/user-attachments/assets/c28075f1-445c-4ac7-9b2f-7caba7cab306)

