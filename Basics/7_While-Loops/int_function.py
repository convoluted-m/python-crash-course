## int() function converts the input string to a numerical value

# # Example 1. Age
# age = input("How old are you? ")
# age = int(age)
# print(f"\nI see your are, {age}!")

# Example 2. Height
height = input("How tall are you, in cm? ")
height = int(height)
if height >= 150:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")