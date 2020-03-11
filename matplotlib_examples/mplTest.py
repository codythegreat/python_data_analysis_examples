import matplotlib.pyplot as plt
import numpy as np

# create an array from 1-5
x = np.arange(1, 6)
y = x**3

# use 10x5 as the figure size
plt.figure(figsize=(10,5))

# plot two sets of data, one with blue dots and another with red triangles
plt.plot([1,2,3,4,5], [1,4,3,9,21], "bo", x, y, "r^")

# set title
plt.title("Sales and Employee Count by Quarter")

# set the legend
plt.legend(["Employee Count", "Sales"])

# set the XY labels
plt.xlabel("Quarter")
plt.ylabel("Dollars (per thousand)")

# finally, show the figures
plt.show()