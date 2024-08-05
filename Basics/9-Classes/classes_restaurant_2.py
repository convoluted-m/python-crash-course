## Modified Restaurant class to include information about customers served
# Added  new attribute self.number_served with a default value
# and a method set_number_served to update the value 

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        # Add a new attirbute with a default value
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called '{self.name}' and it serves {self.type} food.")

    def open_restaurant(self):
        print(f"'{self.name}' is currently open.")

    # Add a method to change the number of customers
    def set_number_served(self, customers):
        self.number_served = customers

    # Add a method to print the default value
    def read_number_served(self):
        print(f"The restaurant has served {self.number_served} customers.")

restaurant = Restaurant('Roots', 'vegetarian')

# Change the value directly: restaurant.number_served = 10
# Change the value with a method - call the  method
restaurant.set_number_served(10)

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_number_served()




