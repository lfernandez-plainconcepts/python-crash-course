print("Given two numbers, this program will divide the first number by the second number.")
print("Enter 'q' to quit at any time.")

while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("Enter the second number: ")5
    if second_number.lower() == 'q':
        break

    try:
        result = float(first_number) / float(second_number)
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("You cannot divide by zero. Please enter a different second number.")
        # pass
    else:
        print(
            f"The result of dividing {first_number} by {second_number} is: {result}")
