range_2_to_4 = range(2,5)
range_0_to_4 = range(5)

# Prints the range object, not the numbers
print(range_2_to_4)

# Use in loops
for value in range(2,5):
    print(value)


# Convert to list
numbers = list(range_2_to_4)
print(numbers)

# Step through a range
even_numbers = list(range(1,20,2))
print("Even numbers:", even_numbers)
