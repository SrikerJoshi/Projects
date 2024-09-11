import streamlit as st
import google.generativeai as ai

# API key configuration
Api_key = "Your api key"

# Load personal information from file
def load_personal_info(filename):
    with open(filename, 'r') as file:
        personal_info = file.read()
    return personal_info

personal_info = load_personal_info("personal_info.txt")

# Configure Google Generative AI
ai.configure(api_key=Api_key)

# Initialize the Generative Model and start a chat session
model = ai.GenerativeModel("gemini-1.0-pro-latest")
chat = model.start_chat()

# Define Streamlit app
st.title("Sriker Joshi Chatbot")
st.write("I am here to help you with providing information about Sriker Joshi. Feel free to ask me anything related to Sriker Joshi's background, interests, education, and more!")
st.write("Type 'clear' to reset the chat, and 'bye', 'exit', or 'quit' to close the conversation.")

# Initialize session state for conversation history and input box
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

if 'chat_active' not in st.session_state:
    st.session_state.chat_active = True

# Handle user input
def handle_input(user_input):
    if user_input.lower() in ['bye', 'exit', 'quit']:
        st.session_state.conversation.append(f"You: {user_input}")
        st.session_state.conversation.append("Bot: Exiting the chatbot. The context has been reset.")
        st.session_state.conversation = []
        st.session_state.user_input = ""
        st.session_state.chat_active = False  # Set chat to inactive
        return

    if user_input.lower() in ['clear', 'reset']:
        st.session_state.conversation = []
        st.session_state.conversation.append("Chatbot: Chat has been cleared. Feel free to ask your questions again.")
        st.session_state.user_input = ""
        return

    context_message = f"Here is some information about Sriker Joshi:{personal_info}\nUser's question: {user_input}\n\nAnswer"
    
    try:
        # Send message using chat session
        response = chat.send_message(context_message)
        response_text = response.text.strip().lower()  # Ensure to access 'text' correctly

        if any(phrase in response_text for phrase in ["the provided", "the information provided, the provided text"]):
            response_text = "I am sorry, but Sriker's database doesn't contain this information. Please feel free to ask other things about Sriker."
        
    except Exception as e:
        response_text = f"I am sorry, but an error occurred while processing your request: {e}"
    
    st.session_state.conversation.append(f"You: {user_input}")
    st.session_state.conversation.append(f"Bot: {response_text}")

# Display conversation history
for line in st.session_state.conversation:
    st.write(line)

# Input box for new questions
def submit_input():
    if st.session_state.user_input:
        handle_input(st.session_state.user_input)
        if st.session_state.chat_active:
            st.session_state.user_input = ""  # Clear input box after submission

# Show input box only if chat is active
if st.session_state.chat_active:
    st.text_input("You:", key="user_input", value=st.session_state.user_input, on_change=submit_input)
else:
    st.write("The chat has ended. have a good day, please refresh the page to start chat again.")
