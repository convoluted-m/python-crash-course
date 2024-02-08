## Accessing elements in the list
bikes = ['mountain bike', 'road bike', 'BMX bike', 'electric bike', 'hybrid bike', 'gravel bike', 'city bike', 'folding bike']
print(bikes)
print(bikes[0])

# Using string methods with elements of the list
print(bikes[0].title())

# Accessing the last element in the list: use [-1]
print(bikes[-1])
# The same principle applies to the element that is second from the end, etc. 
print(bikes[-2])

# Using individual values from a list
message = f"My favourite type of bike is {bikes[0].title()}."
print(message)

## Practice
# Accessing elements in the list 
funny_dog_names = ['Hairy Pawter', 'Chewbarka', 'Furdinand', 'Dogstoevsky', 'Bark Twain']
print(funny_dog_names[2])
# Using individual values
message_1 = f"Gnocchi's favourite book is '{funny_dog_names[0]}'."
print(message_1)
message_2 = f"Capo spent the whole night reading {funny_dog_names[4]}."
print(message_2)