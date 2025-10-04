Basic NLP Rule-Based Chatbot 
 Objective

Build a simple rule-based chatbot in Python that demonstrates the basic structure of NLP (Natural Language Processing) using only if-elif-else rules.

🛠 Tools Used

Python 3.x (no extra libraries required)

 Project Files

nlp_rule_based_chatbot.py → Main chatbot script.

 How It Works

The chatbot uses simple NLP steps to understand user input:

Normalization – Converts input to lowercase and removes extra spaces.

Tokenization – Splits the sentence into individual words using .split().

Keyword Matching – Looks for specific keywords like "hello", "name", "weather", etc.

Rule-Based Logic – Uses if-elif-else conditions to generate responses.

 Running the Chatbot

Save the script as nlp_rule_based_chatbot.py.

Run the program:

python nlp_rule_based_chatbot.py


Chat with the bot! Type bye to exit.

 Example Interaction
Hello! I am ChatBot 🤖. Type 'bye' to exit.

You: hello
Bot: Hello! How can I help you today?

You: what is your name
Bot: I am a simple chatbot created using Python and basic NLP rules.

You: how are you
Bot: I’m doing great! Thanks for asking. How about you?

You: what about the weather
Bot: I cannot check the weather yet, but it’s always sunny in my code! 😃

You: bye
Bot: Goodbye! Have a nice day 🙂

 Outcome

Understand how basic NLP structure works.

Learn text preprocessing (normalization, tokenization).

See how rule-based chatbots handle user queries using keyword matching
