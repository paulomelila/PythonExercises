# importing external libraries

import numpy as np # NumPy is a powerful library for numerical computations in Python
import matplotlib.pyplot as plt # Matplotlib is a popular library for creating static, animated, and interactive visualizations in Python

# Setting a seed for reproducibility of random numbers
np.random.seed(1)

# Generate 1000 random numbers with mean 20 and standard deviation 2
data = np.random.normal(loc=20, scale=2, size=1000)

# Plot a histogram of the generated data
plt.hist(data, color='lightblue', ec='red')

# Add title and labels to the plot
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show() # Display the plot