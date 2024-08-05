# # Tuples - immutable lists of values. Use when values should not be changed throughout the life of the program.
# dimensions = (100, 50)
# print(dimensions)
# print(dimensions[0])
# print(dimensions[1])

# # looping through all values in a tuple
# for dimension in dimensions:
#     print(dimension)

# # Writing over a tuple - reassigning the variable
# dimensions = (100, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (200, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# Exercise 
foods = ('sandwich', 'croissant', 'apple', 'banana', 'chocolate bar')
print("\nThe buffet offers the following foods:")
for food in foods:
    print(food)

# rewriting the tuple
foods = ('sandwich', 'wrap', 'croissant', 'doughnut', 'apple')
print("\nThe new buffet offer:")
for food in foods:
    print(food)

