# Collect names of all the guests and store them in a guest book (txt file)

# Import a library for working with files
from pathlib import Path

# Prompt the user to provide the guest names
print("Please log all the guest names in the guest book.")
print("Say 'done' when you're done.")
name = input("Guest name: ")

# Write the guest names in a file
path = Path('guest_book.txt')
path.write_text(name)