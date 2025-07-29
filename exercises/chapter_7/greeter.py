prompt = "If you share your name, I can personalize the messages you see."
prompt += "\nWhat is your name? "

user_name = input(prompt)

print(f"\nHello {user_name}!")

user_age = int(input("How old are you? "))

print(f"You are {user_age} years old.")
if user_age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

