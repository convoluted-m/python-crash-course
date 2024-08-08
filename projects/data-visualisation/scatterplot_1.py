# Plotting single points with Matplotlib and scatter()

# import the pyplot module
import matplotlib.pyplot as plt

# Prepare the data to plot
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# use a built-in style for the plot
plt.style.use('seaborn-v0_8')

# Generate a plot
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set the chart title and label the axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of the tick labels
ax.tick_params(labelsize=14)

# Display the plot
plt.show()
