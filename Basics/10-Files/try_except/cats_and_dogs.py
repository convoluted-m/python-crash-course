# Write a program that reads these files and print the contents of the file
# Wrap your code in a try-except block to catch the FileNotFound error


from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    print(f"Reading {filename}")
    path = Path(filename)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry, I couldn't find the file.")
    else:
        print(contents)