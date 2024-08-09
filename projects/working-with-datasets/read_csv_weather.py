## Read weather data from a csv file

# Import the Path class from pathlib & the csv module
from pathlib import Path
import csv

# Build a path object pointing to the file
path = Path('weather-data/sitka_weather_07-2021_simple.csv')
# Read the file contents & get all lines
lines = path.read_text().splitlines()

# Build a reader object to parse lines in the file
reader = csv.reader(lines)
# Return the next line of the file
header_row = next(reader)


# Explore data - print headers and their positions
for index, column_header in enumerate(header_row):
    print(index, column_header)


# Read the high temp
highs = []
# Loop over the lines in the file and pull data from index 4
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)