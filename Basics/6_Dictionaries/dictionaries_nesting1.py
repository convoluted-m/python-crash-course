### Dictionaries in a list

# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("\n")


# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens using range()function and append them to the list
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("\n")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# change colour of 3 aliens to yellow, medium-speed,worth 10 points
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("\n")

# change yellow aliens into red, fast-moving, worth 15 points
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("\n")