import matplotlib.pyplot as plt
import numpy as np

# adjust size of figure to better fit screen
plt.figure(figsize=(8,7))

# create a 2x1 subplot using a green line to plot the data points
plt.subplot(2, 1, 1)
x1 = [1,2,3,4,5]
y1 = [239, 431, 454, 555, 334]
plt.plot(x1, y1, "g-")
plt.title("Joey Hunger Level") # my cat

# create a 2x1 subplot using a red line to plot the data points
plt.subplot(2,1,2)
x2 = [1,2,3,4,5]
y2 = [2000, 6000, 12000, 24000, 50000]
plt.plot(x2, y2, "r-")
plt.title("Chrome Ram Usage")

# Give the figure a title and show the figure
plt.suptitle("Some Data:")
plt.show()