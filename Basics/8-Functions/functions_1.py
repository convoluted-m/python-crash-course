## A function is a named block of code used to perform a certain task
# Define the function and pass a parameter (variable)
def greet_user(username):                 # greet user by name
    """display simple greetng"""          # docstring defines what the function does
    print(f"Hey, {username.title()}!")  

# Call (execute) the function
greet_user('Buster')                       # argument "Dusty" is passed to the function (value)


## A function can have multiple parameters
# Positional arguments are matched in the order they are provided
def describe_activity(activity_type, activity_location):
    print(f"I went for a {activity_type} to {activity_location}.")

describe_activity('run', 'Nendrum')


## You can call a function with different arguments
def describe_activity(activity_type, activity_location):
    print(f"I went for a {activity_type} to {activity_location}.")

describe_activity('walk', 'Mount Stewart')
describe_activity('ride', 'Castlewellan')


## Keyword arguments are name-value pairs that you pass to a function
def describe_activity(activity_type, activity_location):
    print(f"I went for a {activity_type} to {activity_location}.")

describe_activity(activity_type='swim', activity_location='Ballywalter')


## Default values - if we define a default value for an argument there's no need to provide it later
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='Gnocchi')

# if we do provide the explicit value though, then the default vcalue will be ignored
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='doggo', pet_name='Gnocchi')

## Returning values with a return statement
def city_country(city, country):
    pair = f"{city}, {country}"
    return pair.title()

location_1 = city_country('vancouver', 'canada')
print(location_1)

## Returning values with an optional argument (middle name)
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

character = get_formatted_name('konwalia', 'rozycka')
print(character)

character = get_formatted_name('grace', 'posy', 'anne') 
print(character)
