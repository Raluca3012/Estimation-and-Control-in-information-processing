import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 1, 1000)

plt.hist(x, bins=30)
plt.title("Histogram of X ~ Uniform(0,1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()