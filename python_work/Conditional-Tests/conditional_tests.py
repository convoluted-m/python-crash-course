# checking for equality ==
car = 'Mini Cooper'
if car == 'Mini Cooper':
    print(car)
else:
    print('\nFalse')

# checking for inequality !=
colour = 'red'
if colour != 'red':
    print("Not red!")
else: 
    print("\nIt's red!")

# numerical comparisons
answer = 4
if answer == 5:
    print("Well done!")
else: 
    print("\nThat's not the correct answer. Please try again!")

age = 19
if age > 18:
    print("\nWelcome!")
else:
    print("\nSorry, you must be over 18 to view this conteny.")

# multiple conditions - and/or
age = 30
age >=18 and age < 40 # can also use parentheses (age >=18) and (age < 40)

# Checking if a Value Is in a List - in
# Returns True/False
colours = ["sea green", "turquoise", "lime", "sage", "moss"]
print("sea green" in colours)

# Checking if a Value is not in a List - not in
banned_users = ['Tom', 'David']
user = 'Pat'
if user not in banned_users:
    print(f"{user}, welcome to the group!")

good_moods = ["happy", "calm", "energetic"]
mood = "calm"
if mood in good_moods:
    print("\nGlad you are feeling good today.")

bad_moods = ["uneasy", "sad", "worried"]
mood = "uneasy"
if mood in bad_moods:
    print ("I'm sorry you are feeling this way. Would you like to chat more about it?")

# Boolean Expressions - True or False
flower = "daffodil"
print(flower == 'daffodil')


# Simple if statement
age = 19
if age >= 18:
    print("\nYou are old enough to vote!\n")


# If statement with a for loop
cars = ['audi', 'bmw', 'subaru', 'mini cooper']

for car in cars:
    if car == 'bmw':
        print(car.upper())

    else:
        print(car.title())

# if-else statements (execute one of two possible actions)
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")       

# if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# more concise
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"\nYour admission cost is ${price}.")

# multiple elif blocks
age = 16
if age < 16:
    price = 10
elif age < 20:
    price = 25
elif age < 65:
    price = 10
else:
    price = 20
print(f"The course cos is ${price}.")

# Testing Multiple Conditions
# When it’s important to check all conditions, use a series of if statements with no elif or else blocks
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
      print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings: print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")