import numpy as np
import matplotlib.pyplot as plt

X1 = np.random.normal(0, 0.5, 1000)
X2 = np.random.normal(0, 1.0, 1000)
X3 = np.random.normal(0, 2.0, 1000)

print("Variance X1:", np.var(X1))
print("Variance X2:", np.var(X2))
print("Variance X3:", np.var(X3))

plt.figure(figsize=(8, 5))
plt.hist(X1, bins=30)
plt.title("Gaussian Noise: mean=0, std=0.5")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(X2, bins=30)
plt.title("Gaussian Noise: mean=0, std=1")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(X3, bins=30)
plt.title("Gaussian Noise: mean=0, std=2")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()