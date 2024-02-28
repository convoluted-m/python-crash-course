# DICTIONARIES
# define a dict
alien = {}

# Sample dictionary of key-value pairs
alien = {'color': 'sea green', 'points': 5}

# Use key to access the value with dict_name[key]
print(alien['color'])
print(alien['points'])

# Another example of value retrieval
new_points = alien['points']
print(f"You just earned {new_points} points!")

# Adding more key-value pairs
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

# Modifying values
alien = {'color': 'sea green'}
print(f"The alien is {alien['color']}.")
# key in square brackets and the new value you want associated with it
alien['color'] = 'green'
print(f"The alien is now {alien['color']}.")

# Tracking the alien position at diferent speeds
alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien['x_position']}")

# Determine how far to move the alien based on its current speed
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':      
    x_increment = 2
else:
# This must be a fast alien
      x_increment = 3
# The new position is the old position plus the increment
alien['x_position'] = alien['x_position'] + x_increment
print(f"New position: {alien['x_position']}")

# Change speed 
# alien['speed'] = 'fast'

# Removing Key-Value pairs permanently with del statement
alien_0 = {'color': 'pink', 'points': 7}
print(alien_0)
del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
favorite_sweets = {
    'jen': 'cookie',
    'sarah': 'candy',
    'ed': 'ice cream',
    'phil': 'chocolate',
    }

print(favorite_sweets)

# accessing values and assigning to variables
sweet = favorite_sweets['sarah']
print(f"Sarah's favorite sweet is {sweet}.")

# Using get() method to access values
teletubby = {
  "name": "Tinky Winky",
  "colour": "purple",
  "personality": "dreamer"
}

quality = teletubby.get("personality")
print(quality)

# If no value when accessing
attribute_value = teletubby.get('attribute', 'No point value assigned.')
print(attribute_value)
# add value 
teletubby['attribute'] = 'red bag'
print(teletubby['attribute'])




 

