# Write a while loop that prompts users for their name. 
# Collect all names and write them  to a file  guest_book.txt. 

# Import the pathlib library for working with files
from pathlib import Path

# provide the path to the file to be created
path = Path('guest_book.txt')

# Prompt the user to provide the guest names
prompt = ("Hi, what's your name? ")
prompt += ("Say 'done' if you're the last guest. ")

# Crate a list to store guest names
guest_names=[]

while True:
    name = input(prompt)
    if name == "done":
        break

    print("Thanks! Added your name to the guest book.")
    guest_names.append(name)

file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

# Write the guest names in a file
path.write_text(file_string)