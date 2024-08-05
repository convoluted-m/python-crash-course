# A function that returns a neatly formatted city-country pair
"""A collection of functions for working with cities."""

def get_city_country (city, country, population=0):
    """Return a single string representing a city-country pair like 'Santiago, Chile' ."""
    if population:
        full_location = f"{city}, {country}, {population}"
    else:
        full_location = f"{city}, {country}"
    return full_location.title()