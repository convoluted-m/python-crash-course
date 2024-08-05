## Function displaying my current mood
def display_mood(mood):
    print(f"I'm feeling {mood} today.")

display_mood('so-so')

## Customised T-shirt function
# Using positional arguments
def make_shirt(size, colour, message):
    print(f"You've ordered a T-shirt in size {size}, in {colour} colour, with the following message printed on it: {message}.")

make_shirt('S', 'pink', 'Make life richer')


# Using keyword arguments
def make_shirt(size, colour, message):
    print(f"You've ordered a T-shirt in size {size}, in {colour} colour, with the following message printed on it: {message}.")

make_shirt(size='M', colour='green', message='Grow your roots')

## Using default values
def make_shirt(size, colour, message="Ride the waves"):
    print(f"You've ordered a T-shirt in size {size}, in {colour} colour, with the following message printed on it: {message}.")

make_shirt(size='L', colour='blue',)

## Mixed values
def make_shirt(size, colour, message="Shine your light"):
    print(f"You've ordered a T-shirt in size {size}, in {colour} colour, with the following message printed on it: {message}.")

make_shirt(size='L', colour='yellow',)
make_shirt(size='M', colour='orange',)
make_shirt(size='S', colour='purple', message='Attract')
