# Using Python methods with strings
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# f-strings. Format strings by replacing a variable name with its value
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

