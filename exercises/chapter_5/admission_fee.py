ages = [1, 6, 25, 66]

for age in ages:
    print(f"Age: {age}")

    if age < 4:
        message = "Babies enter for free!"
        price = 0
    elif age < 18:
        message = "Child admission fee"
        price = 15
    elif age < 65:
        message = "Adult admission fee"
        price = 40
    else:
        message = "Senior admission fee"
        price = 20

    print(f"{message}: {price}€")
