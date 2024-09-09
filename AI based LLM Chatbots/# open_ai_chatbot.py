
import streamlit as st
from langchain.llms import OpenAI
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory

# Initialize LLM and memory
llm = OpenAI(api_key="your_openai_api_key", model="gpt-4")
memory = ConversationBufferMemory()

# Define prompt template
prompt = PromptTemplate(template="You are a helpful assistant. Answer the following question: {question}", input_variables=["question"])

# Create chain
chain = LLMChain(prompt_template=prompt, llm=llm, memory=memory)

# Streamlit UI
st.title("Chatbot Interface")
user_input = st.text_input("You:", key="user_input")

if user_input:
    response = chain.run(question=user_input)
    st.write(f"Bot: {response}")

    # Optionally, save the conversation
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    st.session_state.conversation.append(f"You: {user_input}")
    st.session_state.conversation.append(f"Bot: {response}")

    # Display conversation history
    for line in st.session_state.conversation:
        st.write(line)
