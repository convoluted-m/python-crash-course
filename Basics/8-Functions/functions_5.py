## Passing an arbitrary number of arguments to a function
def make_porridge(*ingredients):
    print(ingredients)

make_porridge('oats')
make_porridge('oats', 'milk', 'chocolate', 'hazelnuts')


## The same but using a while loop
def make_porridge(*ingredients):
    print(f"\nMaking your porridge with:")
    for ingredient in ingredients:
        print(f" - {ingredient}")

make_porridge('oats', 'oat milk', 'honey')
make_porridge('oats', 'soy milk', 'chocolate', 'hazelnuts')


##  Using arbirrary keyword arguments - collecting unknown user info
def create_profile(name, **user_info):
    user_info['name'] = name
    return user_info
user_profile = create_profile('fiora',
                              instrument='horn')
print(user_profile)