# Import the necessary library
import matplotlib.pyplot as plt

# Define the data for the pie chart
values = [15, 35, 5, 45]
labels = 'Oranges', 'Apples', 'Pears', 'Strawberries'
colors = {'r', 'g', 'b', 'r'}

# Create a pie chart with the given data, labels, and colors
plt.pie(values, labels=labels, colors=colors)

# Display the plot
plt.show()