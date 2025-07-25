cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

# Sort the list in alphabetical order
cars.sort()
print("Sorted cars:", cars)

# Sort the list in reverse alphabetical order
cars.sort(reverse=True)
print("Reverse sorted cars:", cars)

# Keep list order
print(sorted(cars))
print(sorted(cars, reverse=True))

# Reverse the order of the list
cars.reverse()
print("Reversed cars:", cars)