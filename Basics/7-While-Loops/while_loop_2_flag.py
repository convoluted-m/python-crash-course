# Use a flag variable to determine if the program is active - 
# - run while the flag is set to True, stop when any event sets it to False
# while statement needs to check only one condition if the flag is currently True

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# use flag to indicate whether the program is in an active state
active = True

while active:
    message = input(prompt)
    if message == 'quit':
          active = False
    else:
          print(message)
