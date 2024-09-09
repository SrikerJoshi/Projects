from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = ''' 

Answer the question below
here is the conversation history : {context}

question : {Question}

Answer :
'''

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def load_file_content(filename):
    """Load the content of the specified text file."""
    with open(filename, 'r') as file:
        return file.read()
    
def handle_convo(file_content):
    context = file_content
    print("\nwelcome to my chatbot using LLama and langchain, type 'exit' to exit out of chatbot\n\nYou can use this chatbot to know info about sriker joshi\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the chatbot. Context will be reset.")
            context = file_content  # Reset context to initial content after exiting
            break
        
        result = chain.invoke({"context": context, "Question" : user_input})
        print("chatbot: ", result)
        context += f"\nUser: {user_input}\n chatbot: {result}"

if __name__=="__main__":

    file_content = load_file_content("personal_info.txt")

    handle_convo(file_content)

 
