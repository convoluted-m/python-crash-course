## Modifying list elements
pizza_ingredients = ['tomatoes', 'cheese', 'mushrooms', 'pepperoni', 'onion', 'jalapenos']
print(pizza_ingredients)

# Changing elements
pizza_ingredients[0] = 'tomato sauce'
print(pizza_ingredients)

# Adding elements with the append() method
pizza_ingredients.append('garlic flakes')
print(pizza_ingredients)

# Inserting elements with the insert() method
pizza_ingredients.insert(0, 'dough')
print(pizza_ingredients)

# Removing elements with the del statement
del pizza_ingredients[0]
print(pizza_ingredients)

# Removing elements with the pop() method and keeping the value
popped_ingredient = pizza_ingredients.pop()
print(pizza_ingredients)
print(popped_ingredient)

# Removing the value from the list, not knowing the index: remove() method
pizza_ingredients.remove('onion')
print(pizza_ingredients)
not_available = 'jalapenos'
pizza_ingredients.remove(not_available)
print(f"Sorry, {not_available.title()} are not available at the moment.")