## Classes describe real-world things
# Classes allow to create objects based on them (instances).
# All the objects in the class share the same attributes.
# Classes are part of object-oriented programming.

## Define the class
class Dog:
    """An attempt to represent a dog."""
    
# Create a new instance based on the class using the init() method
# Provide parameters (self doesn't need a value provided)
    def __init__(self, name, age):                      
        """Initialize attributes to describe a dog."""
        # Take the value associated with the parameter and assign it to the variable  
        # Variables accessible through instances are called attributes
        self.name = name 
        self.age = age     

# Define the other methods (these only need the self parameter)
    def sleep(self):
        """Simulate a dog sleeping."""
        print(f"{self.name} is sleeping.")

    def run(self):
        """Simulate running."""
        print(f"{self.name} is running!")

## Create an individual instance from the class to represent a specific dog
# Call the init() method with the arguments in brackets 
boy_dog = Dog('Capo', 5)     
print(f"Our dog's name is {boy_dog.name}.")
print(f"Our dog is {boy_dog.age} years old.")

# Call the other methods
boy_dog.sleep()
boy_dog.run()

## Create another instance of the same class
girl_dog = Dog('Gnocchi', 5)     
print(f"Our dog's name is {girl_dog.name}.")
print(f"Our dog is {girl_dog.age} years old.")

# Call the other methods
girl_dog.sleep()
girl_dog.run()