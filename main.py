
"""
@author: Brad Duy
"""

import ollama

def ai_assistant():
    modes = {
        '1': 'Coding Assistant',
        '2': 'Sentiment Analysis',
        '3': 'Question Answering'
    }
    
    init_messages = {
        '1': 'You are an AI coding assistant expert in various programming languages and software development practices.',
        '2': 'You are an AI sentiment analyzer. Analyze the sentiment of the given text and categorize it as positive, negative, or neutral.',
        '3': 'You are an AI assistant specialized in answering questions on a wide range of topics.'
    }
    
    init_examples = {
        '1': 'What is error for this array in python? conversation = [1,2,3, . Please fix it.',
        '2': 'I like drinking Vietnamese coffee since I am Viet.',
        '3': 'How many days are in a year?'
    }

    print("Welcome to the AI Assistant! Please select a mode:")
    for key, value in modes.items():
        print(f"{key}: {value}")

    mode = input("Enter the number of your chosen mode: ")
    while mode not in modes:
        mode = input("Invalid input. Please enter 1, 2, or 3: ")

    init_mess = init_messages[mode]
    conversation = []

    response = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'system',
            'content': init_mess,
        },
    ])

    conversation.append({'role': 'system', 'content': init_mess})
    conversation.append({'role': 'assistant', 'content': response['message']['content']})

    print(f"\nAI Assistant ({modes[mode]} mode): Hello! How can I assist you today?")
    print(f"\nIf you are not familiar with AI. This is prompt example for you selection: \n --- {init_examples[mode]} ---")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"AI Assistant: Goodbye! Thank you for using the {modes[mode]} mode.")
            break

        if mode == '2':  # Sentiment Analysis mode
            user_input = f"Analyze the sentiment of the following text: '{user_input}'"
        elif mode == '3':  # Question Answering mode
            user_input = f"Please answer the following question: {user_input}"

        response = ollama.chat(model='llama3.1', messages=conversation + [
            {
                'role': 'user',
                'content': user_input,
            },
        ])

        conversation.append({'role': 'user', 'content': user_input})
        conversation.append({'role': 'assistant', 'content': response['message']['content']})

        print(f"AI Assistant: {response['message']['content']}")

    print("\nWould you like to use another mode? (yes/no)")
    restart = input().lower()
    if restart == 'yes':
        ai_assistant()
    else:
        print("Thank you for using the AI Assistant. Goodbye!")


def generate_signature():
    name = "Author: Brad Duy"
    occupation = "AI PhD"
    github_username = "bradduy"

    signature = f"""
                *************************************************
                * {name}                              *            
                * {occupation}                                        *
                * GitHub: https://github.com/{github_username}            *
                *************************************************
                """
    print(signature)


if __name__ == "__main__":
    generate_signature()
    ai_assistant()