import numpy as np

x = np.array([1, 2, 3])
y = np.array([40, 42, 45])

a = 2.5
b = 37.33333333333334

y_pred = a * x + b

r = y - y_pred

error = np.sum(r**2)

print("Predicted values:", y_pred)
print("Residuals:", r)
print("Squared error:", error)