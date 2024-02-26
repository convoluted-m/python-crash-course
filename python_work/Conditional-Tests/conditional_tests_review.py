# ALIEN COLOURS 
# Imagine an alien was just shot down in a game

# if statement
alien_colours = ["green", "yellow", "red"]
alien_colour = "green"
if alien_colour == "green":
    print("You earned 5 points!")

# if statements
alien_colour = "yellow"
if alien_colour == "green":
    print("You earned 5 points!")
if alien_colour!= "green":
    print("You earned 10 points!")
    
# if-else chain
alien_colour = "yellow"
if alien_colour == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!") 

# if-elif- else chain
alien_colour = "red"
if alien_colour == "green":
    print("You earned 5 points!")
elif alien_colour == "yellow":
    print("You earned 10 points!") 
else:
    print("You earned 15 points!")

# STAGES OF LIFE
# if-elif-else chain
age = 33
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# FAV FRUIT
fav_fruit = ["banana", "pomegranate", "redcurrant", "raspberry", "blackberry", "blueberry", "plum"]
fruit = "pomegranate"
if fruit in fav_fruit:
    print(f"You really like {fruit}.")

