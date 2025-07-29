letters = ['a', 'b', 'c', ]

while letters[0:1]:
    action = input("Type 'q' to quit or press Enter to continue: ")
    if action.lower() == 'q':
        break

    print(f"Current letters: {letters}")
    letter = letters.pop(0)
