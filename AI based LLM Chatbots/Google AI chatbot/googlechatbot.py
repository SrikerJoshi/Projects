import os
import google.generativeai as ai

#keep this in .env file do not keep it exposed in the code.

Api_key= "AIzaSyAvtNbQq7RRrbBXjvXPSj-NxLBVM39Aftc"

def load_personal_info(filename):
    with open(filename, 'r') as file:
        personal_info = file.read()
    return personal_info

personal_info = load_personal_info("personal_info.txt")

ai.configure(api_key = Api_key)

model = ai.GenerativeModel("gemini-1.0-pro-latest")
chat = model.start_chat()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print("\nHello! I am here to help you with providing information about Sriker Joshi.\n\nFeel free to ask me anything related to Sriker Joshi's background, interests, education, and more!")
print("\nFeel free to use the words 'clear' or 'reset' to clear your terminal and use 'bye' or 'exit' or quit' to exit from the terminal\n")
fallback_response = "I am sorry, but Sriker's database doesn't contain this information. Please feel free to ask other things about Sriker."

''' if you would like to check explicitly if the request is related to sriker or not use the below function
def is_related_to_sriker(response_text):
    """Check if the response is related to Sriker Joshi."""
    keywords = ["Sriker Joshi", "Sriker", "Joshi", "his background", "his interests", "his education","his job","his projects","his hobbies","his work","data","test"],
    return any(keyword.lower() in response_text.lower() for keyword in keywords)'''

while True:
    message = input("You: ")

    if message.lower() in ['bye','exit','quit']:
        print("Exiting the chatbot. The context has been reset.")
        chat = model.start_chat()  # Reset the chat contex
        break

    context_message = f"Here is some information about Sriker Joshi:{personal_info}, please be a helpful chatbot to tell the user about Sriker's profile.\nUser's question: {message}\n\nAnswer"
    response = chat.send_message(context_message)

    if message.lower() in ['clear', 'reset']:
        clear_terminal()
        print("Chatbot: Chat has been cleared. Feel free to ask your questions again.")
        continue

    try:
        response_text = response.text.strip()
    except AttributeError as e:
        print(f"AttributeError: {e}")
        response_text = fallback_response
    

    if "The provided" in response_text:

        print("Chatbot:", fallback_response)

    else:

        print("Chatbot:", response_text)
        
