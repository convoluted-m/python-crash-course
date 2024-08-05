# List slicing
flowers = ['lavender', 'chamomile', 'poppy', 'buttercup', 'bellflower', 'dandelion']
print(flowers[0:3])
print(flowers[:2])
print(flowers[4:])

#print last element - if you don't know the index number
print(flowers[-1:])

# looping through a slice
print("Here are the first three wildflowers in our list:")
for flower in flowers[:3]:
    print(flower.title())

# copying a list
my_foods = ['pizza', 'burger', 'steak', 'chocolate']
friend_foods =  my_foods[:]
print("My fav foods:")
print(my_foods)
print("Friend's fav foods:")
print(friend_foods)

my_foods.append('potatoes')
friend_foods.append('spinach')
print("My fav foods:")
print(my_foods)
print("Friend's fav foods:")
print(friend_foods)