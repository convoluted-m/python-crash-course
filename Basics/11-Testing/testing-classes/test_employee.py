# Test the Employee class with the @pytest.fixture

import pytest
from employee_class import Employee

# Apply the  fixture decorator and build a function to be used for all tests
@pytest.fixture

def employee():
    """An employee object that will be available to all test functions"""
    employee = Employee("capo", "boi", 60000)
    return employee

def test_give_default_raise(employee):
    """Test if the default raise works properly."""
    employee.give_raise()
    assert employee.salary == 65000

def test_give_custom_raise(employee):
    """Test if a custom raise works properly."""
    employee.give_raise(10000)
    assert employee.salary == 70000