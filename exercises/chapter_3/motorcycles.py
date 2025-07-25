motorcycles = ["hjonda", "yamaha", "suzuki"]
print(motorcycles)

# Update the first item in the list
motorcycles[0] = "honda"
print(motorcycles)

# Add a new item to the end of the list
motorcycles.append("ducati")
print(motorcycles)

# Insert a new item at the beginning of the list
motorcycles.insert(0, "kawasaki")
print(motorcycles)

# ✅ Can insert above the last item
motorcycles.insert(15, "bmw")
print(motorcycles)

# Remove item from the list based on index
del motorcycles[0]
print(motorcycles)

# Also works with negative indexes
del motorcycles[-1]
print(motorcycles)

del motorcycles[1:3]  # Removes items from index 1 to 2
print(motorcycles)

# Remove and retrieve
last_bike = motorcycles.pop()
print(motorcycles)

# Can use indexes
first_bike = motorcycles.pop(0)
print(motorcycles)

# ⚠️ Only removes first occurrence of the item
motorcycles_with_duplicates = ["honda", "yamaha", "suzuki", "honda"]
print(motorcycles_with_duplicates)
motorcycles_with_duplicates.remove("honda")
print(motorcycles_with_duplicates)

