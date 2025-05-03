import streamlit as st
import openai
import os

# Ensure that the OpenAI API key is loaded from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Mental Health Support Chatbot",
    page_icon="❤️",
    layout="centered"
)

# Initialize chat history and context in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I'm here to support you. How are you feeling today?"}
    ]
    
if 'context' not in st.session_state:
    st.session_state.context = None

def add_message(role, content):
    """Add a message to the chat history"""
    st.session_state.chat_history.append({"role": role, "content": content})

def ask_openai(prompt, context=None):
    """Ask OpenAI for a response based on the prompt and context"""
    messages = [{"role": "user", "content": prompt}]
    
    # Add context to the messages if available
    if context:
        messages.insert(0, {"role": "system", "content": context})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if available
        messages=messages
    )
    return response['choices'][0]['message']['content']

def process_user_input(user_input):
    """Process the user input, generate a response using OpenAI"""
    add_message("user", user_input)

    # Generate the response from OpenAI
    response = ask_openai(user_input, context=st.session_state.context)
    
    # Add the assistant's response to the chat history
    add_message("assistant", response)

    # Assume OpenAI returns a mood-related context, set it to session_state
    if "happy" in response.lower():
        st.session_state.context = "Happy"
    elif "sad" in response.lower():
        st.session_state.context = "Sad"
    elif "stressed" in response.lower():
        st.session_state.context = "Stressed"
    else:
        st.session_state.context = "Neutral"

def display_chat():
    """Display the chat history"""
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.write(f'**You:** {message["content"]}')
        elif message["role"] == "assistant":
            st.write(f'**Chatbot:** {message["content"]}')

def handle_quote_button():
    """Handle the 'Give me a quote' button click"""
    quote_prompt = "Give me a motivational quote."
    quote = ask_openai(quote_prompt)
    add_message("quote", quote)

def handle_relaxation_button():
    """Handle the 'Relaxation tips' button click"""
    relaxation_prompt = "Give me a relaxation tip for stress relief."
    tip = ask_openai(relaxation_prompt)
    add_message("relaxation", tip)

def main():
    st.title("Mental Health Support Chatbot")
    st.markdown("""
    This chatbot is here to support your mental wellbeing. Share how you're feeling, 
    and I'll do my best to provide appropriate responses, motivational quotes, 
    or relaxation techniques.
    """)

    # Display current mood (context)
    if st.session_state.context:
        st.markdown(f"**Current mood:** {st.session_state.context}")
    else:
        st.markdown("**Current mood:** Neutral")

    st.subheader("Conversation")
    chat_container = st.container()
    with chat_container:
        display_chat()

    with st.form(key='message_form', clear_on_submit=True):
        user_input = st.text_input("Type your message here:", key="user_input")
        submitted = st.form_submit_button("Send")
        if submitted and user_input:
            process_user_input(user_input)
            st.rerun()

    st.subheader("Quick Actions")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Give me a quote"):
            handle_quote_button()
            st.rerun()
    
    with col2:
        if st.button("Relaxation tips"):
            handle_relaxation_button()
            st.rerun()

    st.markdown("---")
    st.markdown("""
    **About this chatbot:**
    
    This is a simple mental health support chatbot that uses OpenAI to generate responses based on your input.
    
    * Use the text input to share how you're feeling
    * Click "Give me a quote" for motivational quotes
    * Click "Relaxation tips" for stress-relief techniques
    
    Remember, this chatbot is not a substitute for professional mental health support. 
    If you're experiencing serious mental health issues, please reach out to a qualified professional.
    """)

if __name__ == "__main__":
    main()
