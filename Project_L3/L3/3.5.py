import numpy as np
import matplotlib.pyplot as plt

X_gauss = np.random.normal(0, 1, 1000)
X_uniform = np.random.uniform(0, 1, 1000)

plt.hist(X_gauss, bins=30)
plt.title("Gaussian Distribution (mean=0, std=1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.hist(X_uniform, bins=30)
plt.title("Uniform Distribution (0,1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.hist(X_gauss, bins=30, alpha=0.6, label="Gaussian")
plt.hist(X_uniform, bins=30, alpha=0.6, label="Uniform")

plt.title("Gaussian vs Uniform Distribution")
plt.legend()
plt.show()