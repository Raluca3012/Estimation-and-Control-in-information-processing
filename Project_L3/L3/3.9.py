import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(0, 1, 1000)
noise = np.random.normal(0, 0.5, 1000)
Y = 2 * X + noise
cov_matrix = np.cov(X, Y)
covariance = cov_matrix[0, 1]

print("Covariance:", covariance)
plt.scatter(X, Y)
plt.title("Correlation between X and Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()