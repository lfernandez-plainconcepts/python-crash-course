name = "ada lovelace"
print(name.title())
print(name.upper())

name = "ALAN TURING"
print(name.title())
print(name.lower())

# String interpolation / f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())

print(f'Hello, {full_name.title()}!')

# String trimming
print("striped ".rstrip())
print(" stripped".lstrip())
print("  stripped  ".strip())

# Remove prefix and suffix
filename = "python_work/name.py"
print(filename.removeprefix("python_work/"))
print(filename.removesuffix(".py"))