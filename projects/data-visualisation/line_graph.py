# Plot a simple line graph with Matplotlib

# import the pyplot module to generate plots
import matplotlib.pyplot as plt

# prepare the data to plot
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# use a built-in style for the plot
plt.style.use('seaborn-v0_8')

# Generate a plot with the subplots() function (can generate multiple plots in the same figure)
fig, ax = plt.subplots()

# use the plot() method to plot the data and adjust the line's thickness
ax.plot(input_values, squares, linewidth=3)

# Add the chart title and label the axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# open the Matplotlib's viewer and display the plot
plt.show()