### LOOPING THROUGH KEY-VALUE PAIRS
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# Use items() method to return key-value pairs
for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")

# Using variables and for loop for print info from a dictionary
fav_languages = {
    'jen': 'spanish',
    'sarah': 'russian',
    'edward': 'french',
    'phil': 'greek',
    }

for name, language in fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

### LOOPING THROUGH KEYS
# Loop only through the keys using the key() method
for name in fav_languages.keys():
    print(name.title())

# Adding personalized message for friends
# create a friends list
friends = ['phil', 'sarah']
# loop through the dict
for name in fav_languages.keys():
    print(f"Hi {name.title()}.")
# if name is in friend's list, print a special message
    if name in friends:
        language = fav_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Use if statement to print a special message if a key-value pair doesn't exist
if 'erin' not in fav_languages.keys():
    print("Erin, please take our poll!\n")

# Looping Through a Dictionary’s Keys in a Particular Order with sorted() function
for name in sorted(fav_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


### LOOPING THROUGH VALUES
# Looping Through Values using the values() method
print("The following languages have been mentioned:")
for language in fav_languages.values():
    print(language.title())

# To avoid repeated values use set()
fav_colours = {
    'jen': 'black',
    'sarah': 'blue',
    'edward': 'purple',
    'phil': 'black',
    }

for colour in set(fav_colours.values()):
    print(colour)

# Sets - building sets and printing unique elements
colours = {'yellow', 'lime', 'turqouise', 'orange', 'lime'}
print(colours)

