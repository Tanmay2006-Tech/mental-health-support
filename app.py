import streamlit as st
from mood_detector import detect_mood
from response_generator import generate_response
import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


if not openai.api_key:
    st.error("OpenAI API key is missing. Please set the 'OPENAI_API_KEY' environment variable.")

    
st.set_page_config(page_title="Mood-Aware Chatbot", page_icon="💬")
st.title("Mood-Aware Chatbot 🤖")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_mood" not in st.session_state:
    st.session_state.current_mood = "Neutral"


st.sidebar.title("🧠 Current Mood")
st.sidebar.markdown(f"**{st.session_state.current_mood}**")


user_input = st.chat_input("Say something...")

if user_input:
    
    st.session_state.messages.append({"role": "user", "content": user_input})

    
    mood = detect_mood(user_input)
    st.session_state.current_mood = mood  

    
    bot_response = generate_response(mood, user_input)

    
    if not bot_response.strip():
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            bot_response = response.choices[0].message['content']
        except openai.error.OpenAIError as e:
            st.error(f"An error occurred with the OpenAI API: {e}")
            bot_response = "Sorry, I'm having trouble right now. Please try again later."

    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
