import matplotlib.pyplot as plt

# a range of values from 1 through 1000
x_values = range(1, 1001)
# use list comprehension to generate y values by looping through the x-values and squaring each number
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fix, ax = plt.subplots()
# pass the input and the output values to scatter()
ax.scatter(x_values, y_values, color='purple', s=10) # can define the colour

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of Values", fontsize=14)
ax.tick_params(labelsize=14)

# Pass the minimum and maximum values for x and y axes to the axis() method
ax.axis([0, 1100, 0, 1_100_000])
# can change the tick notation to plain
#ax.ticklabel_format(style='plain')

plt.show()