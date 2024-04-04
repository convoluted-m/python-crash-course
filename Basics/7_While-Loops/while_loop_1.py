#  Use the while loop to keep programs running as long as certain conditions remain true 

# Example. Choose when to quit
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# set a variable 'message' as an empty string to keep track of what the user enters 
message = ""

# the loop runs as long as the value of message is not 'quit'
# otherwise the program stops
while message != 'quit':
    message = input(prompt)
   # print the message  only if it does not match the quit value
    if message != 'quit':
        print(message)