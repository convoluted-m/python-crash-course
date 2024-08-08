# Use gradient to emphasise the pattern in the data using a colormap

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fix, ax = plt.subplots()
# make low values a light colour and high values a darker colour 
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) 

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of Values", fontsize=14)
ax.tick_params(labelsize=14)

ax.axis([0, 1100, 0, 1_100_000])

plt.show()

# save a plot automatically instead of showing it in the viewer
#plt.savefig('squares_plot.png', bbox_inches='tight') # second argument trims extra whitespace - optional