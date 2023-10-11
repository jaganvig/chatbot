import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hello|hi|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm good, thanks!", "I'm doing well. How about you?"]
    ],
    [
        r"(.*) your name?",
        ["I am a chatbot.", "You can call me ChatGPT."]
    ],
    [
        r"(.*) (love|like) you",
        ["I love you too!", "That's very sweet!"]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm sorry, I don't have access to weather information."]
    ],
    [
        r"quit",
        ["Goodbye!", "Bye for now.", "See you later!"]
    ]
]

# Add more rules as needed.
chatbot = Chat(pairs, reflections)
def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
if __name__ == "__main__":
    chat_with_bot()

