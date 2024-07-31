# writing multiple lines

from pathlib import Path

# Define a variable that will hold the text
contents = "Capo and Gnocchi love going on adventures.\n"

# add more content to the string
contents+= "They often visit the Park.\n"
contents += "They also love going to Nendrum.\n"
contents += "Occassionaly, they go to the beach."

# define the path and name of the file
path = Path('dog_adventures.txt')

# write the content into the file
path.write_text(contents)

print(contents)