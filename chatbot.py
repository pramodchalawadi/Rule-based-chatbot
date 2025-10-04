# nlp_rule_based_chatbot.py

print("Hello! I am ChatBot 🤖. Type 'bye' to exit.\n")

while True:
    # Take user input and normalize it
    user_input = input("You: ").lower().strip()
    tokens = user_input.split()   # Basic NLP: tokenization

    if any(word in tokens for word in ["hi", "hello", "hey"]):
        print("Bot: Hello! How can I help you today?")

    elif "name" in tokens:
        print("Bot: I am a simple chatbot created using Python and basic NLP rules.")

    elif "how" in tokens and "you" in tokens:
        print("Bot: I’m doing great! Thanks for asking. How about you?")

    elif "weather" in tokens:
        print("Bot: I cannot check the weather yet, but it’s always sunny in my code! 😃")

    elif "help" in tokens:
        print("Bot: You can ask me about my name, how I am, or say hello/bye.")

    elif "bye" in tokens:
        print("Bot: Goodbye! Have a nice day 🙂")
        break

    else:
        print("Bot: Hmm, I didn’t quite get that. Can you try again?")
