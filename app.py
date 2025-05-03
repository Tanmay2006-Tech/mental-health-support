import streamlit as st
from mood_detector import MoodDetector
from response_generator import ResponseGenerator

# Set page configuration
st.set_page_config(
    page_title="Mental Health Support Chatbot",
    page_icon="❤️",
    layout="centered"
)

# Initialize session state for chat history and context if they don't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I'm here to support you. How are you feeling today?"}
    ]
    
if 'context' not in st.session_state:
    st.session_state.context = None

# Initialize mood detector and response generator
mood_detector = MoodDetector()
response_generator = ResponseGenerator()

def add_message(role, content):
    """Add a message to the chat history"""
    st.session_state.chat_history.append({"role": role, "content": content})

def process_user_input(user_input):
    """Process the user input, detect mood, and generate a response"""
    # Add user message to chat history
    add_message("user", user_input)
    
    # Detect mood and context from user input
    mood, context = mood_detector.detect_mood(user_input)
    
    # Store the detected context in session state for future use
    if context:
        st.session_state.context = context
    
    # Generate response based on mood and context
    response = response_generator.get_mood_response(mood, context)
    
    # Add assistant response to chat history
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
    # Get context from session state if available
    context = st.session_state.get('context', None)
    quote = response_generator.get_motivational_quote(context)
    add_message("quote", quote)

def handle_relaxation_button():
    """Handle the 'Relaxation tips' button click"""
    # Get context from session state if available
    context = st.session_state.get('context', None)
    tip = response_generator.get_relaxation_tip(context)
    add_message("relaxation", tip)

# Remove unused callback function

def main():
    # Title and description
    st.title("Mental Health Support Chatbot")
    st.markdown("""
    This chatbot is here to support your mental wellbeing. Share how you're feeling, 
    and I'll do my best to provide appropriate responses, motivational quotes, 
    or relaxation techniques.
    """)
    
    # Display chat history
    st.subheader("Conversation")
    chat_container = st.container()
    with chat_container:
        display_chat()
    
    # User input with form and submit button
    with st.form(key='message_form', clear_on_submit=True):
        user_input = st.text_input("Type your message here:", key="user_input")
        submitted = st.form_submit_button("Send")
        if submitted and user_input:
            process_user_input(user_input)
            st.rerun()
    
    # Action buttons at the bottom (original position)
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
    
    # Add information about the chatbot
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
