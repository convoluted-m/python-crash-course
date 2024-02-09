# List of places I want  see
places = ['Greece', 'South America', 'New Zaeland', 'Canada', 'Norway']
print("Places I want to see:")
print(places) 

# Show the list in the alphabetical order with the sorted() function and then show that the original order hasn't changed 
print("\nPlaces I want to see in the alphabetical order:")
print(sorted(places))
print("\nHere are the places in the original order:")
print(places)

# Reverse the list order (semi-permanent)
places.reverse()
print("\nPlaces to see in a reversed chronological order:")
print(places)
places.reverse()
print("\nPlaces I wanna seee in the original order:")
print(places)

# Sort the list permanently
print("\nPlaces to see sorted alphabetically:")
places.sort()
print(places)

print("\nPlaces to see in a reverse-alphabetical order:")
places.sort(reverse=True)
print(places)

