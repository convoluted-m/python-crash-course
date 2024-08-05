# if item in a list is not available
requested_toppings = ['jalapenos', 'onions', 'garlic']

for requested_topping in requested_toppings:
    if requested_topping == 'garlic':
        print("Sorry, we are out of garlic right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!\n")

# checking item availability
available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!\n")

# hello admin
users = ["Cookie Monster", "Pink Panther", "Kermit", "Count von Count", "Marvin the Martian", "admin"]
for user in users:
   if user == "admin":
       print(f"Hello admin, would you like to see the status report?")
   else:
       print(f"Hello {user}, you are logged in!")

# no users - empty list
username = []
if username in username:
    print(f"Hello {username}, would you like to see the status report?")
else:
    print("\nWe have no users!\n")

# checking usernames
current_users = ["Twilight Sparkle", "Pinkie Pie", "Applejack", "Rarity", "Rainbow Dash"]
new_users = ["Mr. Toad", "Ratty", "Badger", "Mole", "Otter", "Rarity"]

for new_user in new_users:
    if new_user not in current_users:
        print(f"Welcome to our bunch, {new_user}!")
    else:
        print(f"Oops, this username already exists. Please get even more creative!")


# ordinal numbers
numbers = [""]
