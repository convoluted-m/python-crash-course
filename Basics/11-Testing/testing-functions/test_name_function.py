## Testing code with the pytest library
# Unit test - verifies that one specific aspect of a function’s behavior is correct. 
# Test case - a collection of unit tests proving that a function behaves correctly within the full range of situations you expect it to handle. A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations

## Testing the name function
# Write a test function that makes an asserrtion about the correct test result and determines a pass or fail
# Import the function to test
from name_function import get_formatted_name

# Define a test function
# Test functions need to start with "test" followed by an underscore
def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    # Call the function you're testing and pass arguments
    formatted_name = get_formatted_name('janis', 'joplin')
    # aassign the return value to formatted_name and make an assertion (the value should be X)
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
      """Do names like 'Wolfgang Amadeus Mozart' work?"""
      formatted_name = get_formatted_name( 'wolfgang', 'mozart', 'amadeus')
      assert formatted_name == 'Wolfgang Amadeus Mozart'