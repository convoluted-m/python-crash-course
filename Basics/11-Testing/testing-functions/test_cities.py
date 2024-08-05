# Test function the city function

# Import the function to test
from city_functions import get_city_country

# Define a test function
def test_city_country():
    """Does a simple city-country pair work?"""
    formatted_location = get_city_country("belfast", "united kingdom")
    assert formatted_location == 'Belfast, United Kingdom'

def test_city_country_population():
    """Does it work with an optional population argument?"""
    formatted_location = get_city_country('belfast', 'united kingdom', population=345418)
    assert formatted_location == "Belfast, United Kingdom, 345418"