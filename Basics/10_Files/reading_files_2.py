# Relative path to a file - if the text file is in another directory
# ./ path from the current directory 
# ../ up one dir from that python file

from pathlib import Path

path = Path('../Text_Files/harjo_poem.txt')

harjo_poem_contents = path.read_text()

print(harjo_poem_contents)