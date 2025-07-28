numbers = []

for item in range(2):
    if numbers:
        print("The list is not empty.")
    elif not numbers:
        print("The list is empty.")

    print(numbers)
    numbers.append(item)
