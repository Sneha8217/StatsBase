def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if user_input in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"
    elif user_input in ("how are you", "how are you?"):
        return "I'm fine, thanks! How about you?"
    elif user_input in ("i am fine", "fine", "good"):
        return "That's great to hear!"
    elif user_input in ("bye", "goodbye", "exit"):
        return "Goodbye! Have a nice day!"
    elif user_input in ("what is your name", "who are you"):
        return "I'm a simple chatbot created with Python!"
    elif user_input in ("help", "options"):
        return "You can try saying: hello, how are you, bye, what is your name"
    else:
        return "Sorry, I don't understand that. Try saying 'help'."

def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    try:
        while True:
            user_input = input("You: ")
            response = chatbot_response(user_input)
            print("Chatbot:", response)
            if user_input.lower().strip() in ("bye", "goodbye", "exit"):
                break
    except (KeyboardInterrupt, EOFError):
        print("\nChatbot: Goodbye! (exiting)")

if __name__ == "__main__":
    run_chatbot()