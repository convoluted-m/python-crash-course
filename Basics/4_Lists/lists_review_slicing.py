# Slices
teas = ['green tea', 'asam', 'chamomile', 'chai', 'ginger tea', 'oolong']
print(teas)

# Use a slice to print the first three items from that program’s list
print("The first two items in the list are:")
for tea in teas[:2]:
    print(tea.title())

print("The two items in the middle are:")
for tea in teas[3:5]:
    print(tea.title())


print("The last two items are:")
for tea in teas[4:6]:
    print(tea.title())

# Alternative way with a function - not completed
# def print_teas(list_of_teas,slice,message):
#     print(message)
#     for tea in list_of_teas[slice)]:
#         print(tea.title())

# print_teas(teas,":2","The first two items in the list are:")
# print_teas(teas,"3:5","The two items in the middle are:")
    
# Fav pizzas
my_pizzas = ['Margherita', 'Capricciosa', 'Neapolitan', 'Sicilian', 'Marinara']
friend_pizzas = my_pizzas[:]
print(my_pizzas)
print(friend_pizzas)

my_pizzas.append('Prosciutto e funghi')
friend_pizzas.append('Quattro Formaggi')
print("\nMy fav pizzas are:")
for pizza in my_pizzas[:]:
    print(pizza.title())

print("\nMy friend's fav pizzas are:")
for pizza in friend_pizzas[:]:
    print(pizza.title())

# Foods - loops
my_foods = ['pizza', 'burger', 'steak', 'chocolate', 'potatoes']
print("\nHere are my fav foods:")
for food in my_foods[:]:
    print(food.title())
