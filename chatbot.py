import re
import random

# Predefined responses
RESPONSES = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, how about you?", "I'm great!"],
    "what's your name": ["I am a chatbot.", "I'm your friendly assistant.", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I didn't understand that. I'm still developing"]
}

def get_response(user_input, context):
    for pattern, response_list in RESPONSES.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(response_list)
    
    return random.choice(RESPONSES["default"])

def main():
    context = {}
    print("Advanced Chatbot: Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input, context)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
