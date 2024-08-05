# A program that calls the function collecting a city-country pair information and asks for the user's input

# import the city-country function
from city_functions import get_city_country

# print statement to tell the user how to quit the program
print("Enter 'q' to quit.")

# While loop asking for user's input
while True:
    city = input("Enter the city: ")
    if city == "q":
        break
    country = input("Enter the country: ")
    if country == "q":
        break
    formatted_location = get_city_country(city, country)
    print(formatted_location)