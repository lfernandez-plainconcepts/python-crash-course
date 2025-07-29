prompt = "Tell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

active = True

while active:
    user_message = input(prompt)

    if user_message.lower() == 'quit':
        active = False
    else:
        print(f"You said: {user_message}")
