# Working with files
# To work with the file contents, we we need to tell the path to the file (location)

# Import Path class from pathlib (library for workingh with files and directories)
from pathlib import Path

# Build a path object representing the file and assign it to the path variable
# Here the text file is in the same directory as the python program so filename is enough
path = Path('whyte_poem.txt')

# Read file contents with the read_text() method (returns the contents as a single string)
whyte_poem_contents = path.read_text()

# Print the poem contents
print(whyte_poem_contents)


