from turtle import color
import matplotlib.pyplot as plt

fig = plt.figure()

names = ['A', 'B', 'C']
values = [19, 50, 29]
values_2 = [48, 19, 41]

ax = fig.add_subplot(211)
ax_2 = fig.add_subplot(212)
 # Sets the title of the sublot on position 1 
ax.set_title('Title')
 # Sets the title of the sublot on position 2
ax_2.set_title('Title_2')

 # Adds subplot on position 1 
ax.set_xlabel('x_label')
 # Adds subplot on position 2
ax.set_ylabel('y_label')

#Label names
ax_2.set_xlabel('x_label')
ax_2.set_ylabel('y_label')

#Make bars with color
ax.bar(names, values, color='goldenrod')
ax_2.bar(names, values_2, color='mediumorchid')

 # Sets the title of the entire figure 
plt.suptitle('Test Plots')
plt.show()