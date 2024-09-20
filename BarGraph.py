# Import the necessary library
import matplotlib.pyplot as plt

# Define the data for the x-axis labels and the corresponding values
names = ['A', 'B', 'C'] 
values = [19, 50, 29] 
values_2 = [27, 15, 34] 

# Create a new figure with a specified size
fig = plt.figure(figsize=(8.0,6.0)) 

# Set the label for the x-axis
plt.xlabel("Label for X") 

# Set the label for the y-axis
plt.ylabel("Label for Y") 

# Create a bar plot for the given data
plt.bar(names, values) 

# Add a legend to the plot
plt.legend(['Data'], loc="upper right") 

# Set the title of the entire figure
plt.suptitle('Test Plots') 

# Display the plot
plt.show()