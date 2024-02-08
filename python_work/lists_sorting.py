# Organnizing Lists
dog_toys = ['badgi', 'foxi', 'octopus', 'brussels', 'blizbee (Franklin)', 'orange blizb', 'fav whistly ball', 'squeaky ball', 'small whistly ball']
print("Here's our toys:")
print(dog_toys)

# PERMANENTLY sorting the list alphabetically using the sort()method 
dog_toys.sort()
print("\nToys in the alphabetical order (permanently):")
print(dog_toys)
# PERMANENT: Reverse alphabetical order with the sort() method by passing the reverse=True argument
dog_toys.sort(reverse=True)
print("\nToys in the reverse order (permanently)")
print(dog_toys)

# TEMPORARILY sorting the list alphabetically using the sorted() function
print("\nToys in the alphabetical order (temp):")
print(sorted(dog_toys))
print("\nToys back in the original  order:")
print(dog_toys)

# SEMI-PERMANENT: Print the list in a reverse order using the reverse() method - can go back to original by reverse() again
dog_toys.reverse()
print("\nToys in the reverse chronological order:")
print(dog_toys)
# change to  a reverse alphabetical order
dog_toys.reverse()
print("\nToys back in the original order:")
print(dog_toys)

# Finding out the length of the list
print(len(dog_toys))
print(f"We have {len(dog_toys)} toys.")