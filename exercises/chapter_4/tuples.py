immutable_numbers = (1, 2, 3, 4, 5)

# Same operations as with lists
print(immutable_numbers[0:3])
print(immutable_numbers[0])

# Single element tuple requires a comma
# to differentiate it from a regular parentheses
single_element_tuple = (1,)
print(single_element_tuple)

# Comprehensions not allowed since tuples are immutable
# Attempting to create a tuple with comprehension will raise an error
immutable_number = (value ** 2 for value in range(1, 6))  # This is incorrect

# Correct way to create a tuple with comprehension
immutable_numbers = tuple(value ** 2 for value in range(1, 6))
print(immutable_numbers)
