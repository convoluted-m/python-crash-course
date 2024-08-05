from pathlib import Path

# prompt user for their name
name = input("What's your name? ")

# Write their name in a file
path = Path('guest.txt')
path.write_text(name)