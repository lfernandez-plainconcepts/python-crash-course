class Dog:
    """A class representing a dog with a name and age."""

    def __init__(self, name, age):
        """Initialize the dog with a name and age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate the dog sitting in response to a command."""
        if hasattr(self, 'happy') and self.happy:
            print(f"{self.name} is now sitting.")
        else:
            print(f"{self.name} is not happy enough to sit.")

    def roll_over(self):
        """Simulate the dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def pet(self):
        """Simulate petting the dog."""
        self.happy = True


my_dog = Dog('Willie', 6)

my_dog.sit()
my_dog.pet()
my_dog.sit()

my_dog.happy = False

print(f"Is {my_dog.name.title()} happy? {my_dog.happy}")
