# range() function
for value in range (1, 6):
    print(value)

#list() function
numbers = list(range(1,6))
print(numbers)

# third argument with range()
even_numbers = list(range(2, 9, 2))
print(even_numbers)

# exponents - each value in the range is raised to the second power and appended to the list
squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)

print(squares)

## more efficient
squares = []
for value in range (1,11):
    squares.append(value**2)

print(squares)

# min, max, sum
digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension - same operations in one line of code
squares = [value**2 for value in range(1,11)]
print(squares)