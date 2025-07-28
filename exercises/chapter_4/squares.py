squares = []
for value in range(1,11):
    squares.append(value ** 2)

print("Squares from 1 to 10:", squares)

squares = [value ** 2 for value in range(1,11)]
print("Squares from 1 to 10 (using list comprehension):", squares)