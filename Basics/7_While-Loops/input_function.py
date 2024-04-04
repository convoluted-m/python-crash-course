## Use input() function for the user to enter some text

# Example 1. 
message = input("Please enter your DOB: ")
print(message)


# Example 2. Enter name
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Example 3 . Greeter
prompt = "\nIf you share your name, I can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")