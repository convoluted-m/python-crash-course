# count to twenty
# for value in range (1, 21):
#    print(value)

# one million
# numbers = list(range (1, 1000001))
# for number in numbers:
#    print(number)

# sum to million
# number_list = list(range (1, 1000001))
# print(min(number_list))
# print(max(number_list))
# print(sum(number_list))

# odd numbers
# odd_numbers = list(range(1, 20, 2))
# for number in odd_numbers:
#    print(number)

# # multiples of 3
# threes = []
# for value in range(3, 30):
#     threes.append(value**2)

# print(threes)

# cubes - number raised to the third power
print(2**3)

# cubes for loop
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# Cube list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)