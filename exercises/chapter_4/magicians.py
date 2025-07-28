# FOR loop
magicians = ['alice', 'david', 'carolina']

# Indentation creates loop scope
for magician in magicians:
    # Inside loop
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Outside loop
print("Thank you, everyone. That was a great magic show!\n")

# ⚠️ 'for' variable still exists out of the loop scope
print(f"I am {magician.title()}, the last magician of the list!") # It works!!!