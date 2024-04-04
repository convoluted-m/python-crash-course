### A List in a Dictionary - Use when you want more than one value to be associated with a single key

## Pizza order
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

## People's fav literary genres
fav_book_genres = {
    'celeste': ['mystery', 'fairy tale'],
    'aslan': ['fantasy'],
    'cedric': ['romance', 'adventure fiction'],
    'fay': ['poetry', 'historical fantasy'],
    }
for name, genres in fav_book_genres.items():
    # check whether  person has one or more  fav genres and print appropriate statement
    if len(genres) <= 1:
        print(f"\n{name.title()}'s favorite genres is:")
    else:
        print(f"\n{name.title()}'s favorite genres are:")

    for genre in genres:
        print(f"\t{genre.title()}")

