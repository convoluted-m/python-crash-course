# Variable printing
message = "Hello Python Crash Course reader!"
print(message)

# Using Python methods with strings: lower, upper, case and title
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

# Add a tab to text
print("Python")
print("\tPython")

# Add a newline
print("Languages:\nPython\nC\nJavaScript")

# Combine tabs and newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# To ensure no whitespace exists at the right side of a string, use the r.strip() method
favourite_language = 'python '
print(favourite_language.rstrip())

# left side - lstrip() 
fav_language1 = ' python'
print(fav_language1.lstrip())

# both sides at once strip()
fav_language2 = ' python '
print(fav_language2.strip())

# using apostrophes
message = "One of Pythn's strengths is its diverse community."
print(message)

# Remove prefixes with the removeprefix() method
convoluted_m_url = 'https://convolutedmeanings.com'
print(convoluted_m_url)
simple_url = convoluted_m_url.removeprefix('https://')
print(simple_url)