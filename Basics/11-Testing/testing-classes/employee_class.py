# Create a class called Employee
class Employee:
    """A class that represents an employee."""

 # Create a new instance of the class and initialize the class attributes
    def __init__(self,first_name, last_name, salary):
        """Initalize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary
    # Define another methods
    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount