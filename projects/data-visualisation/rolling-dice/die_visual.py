## Visualise the results of rolling the dice
# Import the plotly express module to visualise the results of rolling the dice
import plotly.express as px
# Import the die class
from die import Die

# Create an instance of the idea with six sides (default value in the die class)
die = Die()

# Roll the dice 1000 times and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

## Analyse the results
# Create a list to store a number of times each value is rolled
frequencies= []
# Generate all possible results
poss_results = range(1, die.num_sides+1)
# Looop through possible values and count how many times each number appears and append this to frequencies
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

## Visualise the results
# Customise the plot - define the title and axis labels - use a dictionary
title = "Rolling a D6 dice 1000 times"
labels = {'x':'Result', 'y':'Frequency of Result'}
# Create a bar graph with the px.bar() function (title and labels arguments are optional)
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# Label each bar by spacing the tickmarks on the x axis
fig.update_layout(xaxis_dtick=1)

# Render the chart as an HTML file and open in a browser
fig.show()