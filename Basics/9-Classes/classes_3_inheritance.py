## Class inheritance - you can create a class that inherits from another
# Define the parent class
class Car:
    """Represent a car."""
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
        else:
              print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# Define the child class
class ElectricCar(Car):
    """Represents electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        # super() function calls a method from the parent class(gives the parent attributes)
        super().__init__(make, model, year)
        # Define a new attibute for the electric car class and set its value
        self.battery_size = 40

    # Add a method to describe the battery
    def describe_battery(self):
        """Print the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Create an instance of the ElectricCar class
my_electric_car = ElectricCar('nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()