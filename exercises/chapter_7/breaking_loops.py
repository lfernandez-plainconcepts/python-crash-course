iteration = 0

while True:
    user_message = input("Skip / Quit / Go: ")

    if user_message.lower() == 'skip':
        iteration += 1
        continue
    elif user_message.lower() == 'quit':
        break
    else:
        print(f"Iteration {iteration}")
        iteration += 1
