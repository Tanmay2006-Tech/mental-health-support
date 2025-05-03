import streamlit as st
from mood_detector import MoodDetector
from response_generator import ResponseGenerator


st.set_page_config(
    page_title="Mental Health Support Chatbot",
    page_icon="❤️",
    layout="centered"
)


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I'm here to support you. How are you feeling today?"}
    ]
    
if 'context' not in st.session_state:
    st.session_state.context = None


mood_detector = MoodDetector()
response_generator = ResponseGenerator()

def add_message(role, content):
    """Add a message to the chat history"""
    st.session_state.chat_history.append({"role": role, "content": content})

def process_user_input(user_input):
    """Process the user input, detect mood, and generate a response"""
    
    add_message("user", user_input)
    
    
    mood, context = mood_detector.detect_mood(user_input)
    
    
    if context:
        st.session_state.context = context
    
    
    response = response_generator.get_mood_response(mood, context)
    
    
    add_message("assistant", response)

def display_chat():
    """Display the chat history"""
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.write(f'**You:** {message["content"]}')
        elif message["role"] == "quote":
            st.markdown(
                f"""
                <div style="background-color: white; border-radius: 10px; padding: 10px; margin: 10px 0; border: 1px solid #ddd;">
                    <p style="color: black; margin: 0;">{message["content"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif message["role"] == "relaxation":
            st.markdown(
                f"""
                <div style="background-color: white; border-radius: 10px; padding: 10px; margin: 10px 0; border: 1px solid #ddd;">
                    <p style="color: black; margin: 0;">{message["content"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.write(f'**Chatbot:** {message["content"]}')

def handle_quote_button():
    """Handle the 'Give me a quote' button click"""
    
    context = st.session_state.get('context', None)
    quote = response_generator.get_motivational_quote(context)
    add_message("quote", quote)

def handle_relaxation_button():
    """Handle the 'Relaxation tips' button click"""
    
    context = st.session_state.get('context', None)
    tip = response_generator.get_relaxation_tip(context)
    add_message("relaxation", tip)



def main():
    
    st.title("Mental Health Support Chatbot")
    st.markdown("""
    This chatbot is here to support your mental wellbeing. Share how you're feeling, 
    and I'll do my best to provide appropriate responses, motivational quotes, 
    or relaxation techniques.
    """)
    
    
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
    
    This is a simple mental health support chatbot that uses keyword detection to identify your mood and provide appropriate responses.
    
    * Use the text input to share how you're feeling
    * Click "Give me a quote" for motivational quotes
    * Click "Relaxation tips" for stress-relief techniques
    
    Remember, this chatbot is not a substitute for professional mental health support. 
    If you're experiencing serious mental health issues, please reach out to a qualified professional.
    """)

if __name__ == "__main__":
    main()
