import matplotlib.pyplot as plt
import numpy as np

# create an array from 1-5
x = np.arange(1, 6)
y = x**3
# use 10x5 as the figure size
plt.figure(figsize=(10,5))
# plot two sets of data, one with blue dots and another with red triangles
plt.plot([1,2,3,4,5], [1,4,3,9,21], "bo", x, y, "r^")
# set titles and show the figure
plt.title("Title of Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()