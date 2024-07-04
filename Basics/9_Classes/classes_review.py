## Define the class
class Restaurant:
    """An attempt to represent a restaurant."""

#create a new instance of the class
    def __init__(self, name, type):
        """Initialize name and type attributes."""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Provide restaurant name and type.."""
        print(f"The restaurant is called '{self.name}' and it serves {self.type} cuisine.")

    def open_restaurant(self):
        """Indicate if the restaurant is open."""
        print(f"'{self.name}' is currently open.")

## Create an instance from the class
restaurant = Restaurant('Roots', 'vegetarian')
print(f"The restaurant is called '{restaurant.name}'.")
print(f"It serves {restaurant.type} food.")

# Call the other methods
restaurant.describe_restaurant()
restaurant.open_restaurant()