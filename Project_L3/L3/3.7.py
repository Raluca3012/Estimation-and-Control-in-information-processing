import numpy as np
import matplotlib.pyplot as plt

x = 10
noise = np.random.normal(0, 1, 1000)
y = x + noise

print("Mean of measurements:", np.mean(y))
print("Variance of measurements:", np.var(y))

plt.hist(y, bins=30)
plt.title("Sensor Measurement Distribution")
plt.xlabel("Measured value")
plt.ylabel("Frequency")
plt.show()