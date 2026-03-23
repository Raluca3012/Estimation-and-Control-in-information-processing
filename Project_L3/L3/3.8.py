import numpy as np

x_true = 10
noise = np.random.normal(0, 1, 1000)
y = x_true + noise
x_estimated = np.mean(y)
error = x_estimated - x_true

print("True value:", x_true)
print("Estimated value:", x_estimated)
print("Estimation error:", error)