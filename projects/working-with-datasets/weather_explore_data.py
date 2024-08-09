## Read weather data from a csv file and visualise it

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

## Read weather data from a csv file
path = Path('weather-data/sitka_weather_2021_simple.csv')
# Read the file contents & get all lines
lines = path.read_text().splitlines()

# Build a reader object to parse lines in the file
reader = csv.reader(lines)
# Return the next line of the file
header_row = next(reader)

# Explore the data - print headers and their positions
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, high and low temperatures
dates, highs, lows = [], [], []
# Loop over the lines in the file and pull data from index x
for row in reader: 
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

## Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5) # Alpha controls colour's transparency 
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Add shading to emphasize the temp range between highs and lows

# Format the plot
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=10)
fig.autofmt_xdate() # Draw date labels diagonally to prevent overlap
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Show the plot
plt.show()