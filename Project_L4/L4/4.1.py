import numpy as np

y = np.array([21, 22, 23, 24])

x = np.mean(y)
error = y - x
mse = np.mean(error**2)

print("Calibrated temperature:", x)
print("Errors:", error)
print("MSE:", mse)