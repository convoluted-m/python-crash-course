# Passing a list to a function
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['drogo', 'hawk', 'orvyn', 'regina', 'fiora', 'nezetta']
greet_users(usernames)


## Modifying lists with a function
unprinted_patterns = ['honeysuckle ', 'cornflower', 'primrose']
printed_patterns = []

while unprinted_patterns:
      current_pattern= unprinted_patterns.pop()
      print(f"Printing pattern: {current_pattern}")
      printed_patterns.append(current_pattern)
  
print("\nThe following patterns have been printed:")
for printed_pattern in printed_patterns:
    print(printed_pattern)