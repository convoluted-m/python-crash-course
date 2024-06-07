# make a polling program that prompts for participant’s name and response
# store  data gather in a dictionary to connect each response with a particular user

# Define an empty dictionary
responses = {}

# Set a flag to indicate that polling is active
# As long as polling_active is True, it will run the while loop
polling_active = True

# Create a while loop where you prompt the user for response
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What's the best mountain to climb? ")
      # Store the response in the dictionary
    responses[name] = response
      # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
          polling_active = False
  
  
print("\n--- Poll Results ---")
for name, response in responses.items():
      print(f"{name} says the best mountain to climb is {response}.")