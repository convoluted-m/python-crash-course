# Turning a long string into a set of lines with splitlines() method
from pathlib import Path

path = Path('whyte_poem.txt')
contents = path.read_text()

#  Return a list of all lines and assign the list to the variable lines
lines = contents.splitlines()
#  Loop over these lines and print each of them
for line in lines:
    print(line)

# #alternative simpler code
# for line in contents.splitlines():
#     print(line)
