# Personal message
# 1: message + name variable inserted in the print statement
name = "Gerald"
print ("Hello" + " " + name +  ", would you like to learn some Python today?")
# 2: message + name variable inserted in the message
name = "Fifi"
message = "Hello {}, hope you're well!".format(name)
print(message)

# Name cases: lower, upper, case and title
name = "Luna"
print(name.lower())
print(name.upper())
print(name.title())

#  Quoting 1: using the format() method (formats the specified value and inserts them inside the string's placeholder)
quote = "'The body is not a mindless machine; the body and mind are one.'"
quoting = "As dr. Candence B. Pert said, {}".format(quote)
print(quoting)

# Quoting 2: using a variable for author's name
quote_2 = "'Emotions are the nexxus between matter and mind, going back and forth between the two and influencing both.'"
author = "Candence B. Pert"
print("As " + author + " said," + " " + quote_2)

# stripping strings of whitespace
person_name = " Hera "
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

# removing suffixes such as file extensions
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

