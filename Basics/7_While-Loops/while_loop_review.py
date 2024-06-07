# The loop  prompts the user to enter a series of pizza toppings until they enter a 'quit' . 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
prompt = "\nWhat pizza toppings would you like?"
prompt += "\nSay 'done' when you've chosen all of your toppings . "

message = ""

while message != 'done':
    message = input(prompt)
    print("Okay, that's you! Your pizza is being prepared now!")
   # print the message  only if it does not match the quit value
    if message != 'done':
        print(f"Added {message}!")
