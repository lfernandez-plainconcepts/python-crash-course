def describe_pet(pet_name, pet_type='dog'):
    """Function to describe a pet.
    This function prints a description of the pet."""

    print(f"I have a {pet_type} named {pet_name.title()}.")

# Positional arguments
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Keyword arguments
describe_pet(pet_name="Rex", pet_type="dog")
describe_pet(pet_type="hamster", pet_name="Nibbles")