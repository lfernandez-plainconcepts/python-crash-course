def greet_user(user_name="User"):
    """Function to greet the user.
    This function prints a welcome message to the user."""

    print(f"Hello {user_name.title()}, welcome to the program!")


def display_message():
    """Function to display a message."""

    print("This program is designed to greet users.")


greet_user("Peter")
display_message()
