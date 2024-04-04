# Use a flag variable t  determine whether or not the entire program is active
# run while the flag is set to True & stop when any of events sets the value to False
# while statement needs to check only one condition: whether the flag is currently True

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
