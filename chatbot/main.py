import json
import sys
from difflib import get_close_matches

def get_best_matches(user_input: str, knowledge_base: dict) -> str|None:
    best_matches = get_close_matches(user_input, knowledge_base, n=1, cutoff=0.6)

    if best_matches:
        return best_matches[0]

def chat_with_bot(knowledge_base : dict):
    while True:
        user_input: str = input("You : ")
        if user_input.lower() == "exit":
            sys.exit()

        best_match = get_best_matches(user_input, knowledge_base)

        if bot_reply := knowledge_base.get(best_match):
            print(f"Bot : {bot_reply}")
        else:
            print("Bot : I don't about it.")

if __name__ == '__main__':

    with open('knowledge_base.json',"r") as knowledge :
        chatbot_knowledge_base: dict = json.load(knowledge)

    chat_with_bot(chatbot_knowledge_base)




