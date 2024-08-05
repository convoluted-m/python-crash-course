# Taking numerical input
# input() function interprets everything as a string
# Use int() function to convert the input string to a numerical value

# Example: Age
age = input("How old are you? ")
age = int(age)
print(f"I see you are {age}!")

# Example: Height
height = input("\nHow tall are you, in cm? ")
height = int(height)
if height >= 150:
    print(f"\nYaaay, {height} cm is tall enough, so you can ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")