# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Generate a range of values from 0 to 2π with a step of 0.25
range = np.arange(0, math.pi*2, 0.25)

# Calculate the sine values for the generated range
sin = np.sin(range)

# Create a new figure
fig = plt.figure()

# Add a new subplot to the figure
ax = fig.add_axes([0.1, 0.1, 0.75, 0.75])

# Plot the sine values against the range
ax.plot(range, sin)

# Set the labels for the x and y axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the title of the plot
ax.set_title('Sine Wave')

# Set the x-axis ticks and their corresponding labels
ax.set_xticks([0,2,4,6,8])
ax.set_xticklabels(['zero', 'two', 'four', 'six', 'eight'])

# Set the y-axis ticks
ax.set_yticks([-1,0,1])

# Display the plot
plt.show()