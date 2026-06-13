import json
import random

with open("intents.json") as file:
    data = json.load(file)

print("Chatbot Started")
print("Type quit to exit")

while True:
    user = input("You: ")

    if user.lower() == "quit":
        break

    found = False

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if user.lower() == pattern.lower():
                print("Bot:", random.choice(intent["responses"]))
                found = True
                break

    if not found:
        print("Bot: I don't understand.")
