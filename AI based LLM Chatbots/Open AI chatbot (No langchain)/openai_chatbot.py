import openai
import time

openai.api_key = "put your api key here"


def chat_with_gpt(chat_log, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=chat_log
            )
            return response.choices[0].message.content.strip()
        except openai.error.RateLimitError:
            retries += 1
            print(f"Rate limit exceeded. Retrying {retries}/{max_retries}...")
            time.sleep(5)  # Wait before retrying
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {str(e)}")
            break  # Stop if a non-rate-limit error occurs
    return "Failed to get a response due to repeated errors."



if __name__ == "__main__":
    chat_log = []
    # Remembering more posts is more expensive
    n_remembered_post = 2
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', "exit", "bye"]:
            break

        chat_log.append({'role': 'user', 'content': user_input})

        if len(chat_log) > n_remembered_post:
            del chat_log[:len(chat_log)-n_remembered_post]

        response = chat_with_gpt(chat_log)
        print("Chatbot:", response)
        chat_log.append({'role': "assistant", 'content': response})

