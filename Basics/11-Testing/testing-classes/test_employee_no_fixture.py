# Test the Employee class

from employee_class import Employee

def test_give_default_raise():
    """Test if the default raise works properly."""
    employee = Employee("capo", "boi", 60000)
    employee.give_raise()
    assert employee.salary == 65000

def test_give_custom_raise():
    """Test if a custom raise works properly."""
    employee = Employee("gnoc", "gnoc", 60000)
    employee.give_raise(10000)
    assert employee.salary == 70000