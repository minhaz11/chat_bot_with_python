# ChatBot in Python

This project is a simple Python-based chatbot that reads from a knowledge base (`knowledge_base.json`) and interacts with users in a conversational way. The chatbot can understand close matches to user inputs and provides appropriate responses based on its knowledge base. The bot continues to chat until the user types "exit" to end the conversation.

## Features

- **Intelligent Response Matching**: Uses `difflib` to find the closest match to user input, providing a flexible conversational experience.
- **Expandable Knowledge Base**: The chatbot’s responses are defined in an external JSON file (`knowledge_base.json`), making it easy to expand and update.
- **User-Friendly Interaction**: The bot keeps chatting with the user until "exit" is entered, offering an ongoing conversation.

## Requirements

- **Python**: This script is compatible with Python 3.6 or later.
- **Packages**: No external packages required. All dependencies are part of Python's standard library.

## Installation

1. Clone this repository or download the source code files.
2. Ensure you have a `knowledge_base.json` file in the same directory as the code. This file should contain the chatbot's knowledge base in JSON format.

Example of `knowledge_base.json`:
```json
{
    "hi": "Hey there! What can I do for you?",
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm doing great! Thanks for asking. How about you?",
    "exit": "Goodbye! Have a great day!"
}
```

##  Usage
1. Run the chatbot by executing the Python script:  ``python main.py
``
2. Start typing your questions or messages in the console. The bot will respond based on its knowledge base.
3. Type "exit" to end the chat.

## Example Interaction

```You : Hi
Bot : Hey there! What can I do for you?
You : How are you?
Bot : I'm doing great! Thanks for asking. How about you?
You : goodbye
Bot : I don't know about it.
You : exit
```



