## Use input() function for the user to enter some text

# Example: Enter DOB
message = input("Please enter your DOB: ")
print(message)

# Example: Enter name
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Assign a prompt to a variable and pass the variable to the input() function. 
# Use if you want to build your prompt over several lines 
#  += operator takes the string assigned to prompt and adds the new string onto the end

prompt = "\nIf you share your name, I can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")