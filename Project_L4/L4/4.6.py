import numpy as np

errors = np.array([-1, 2, -2])

squared_error = np.sum(errors**2)
absolute_error = np.sum(np.abs(errors))

print("Squared error:", squared_error)
print("Absolute error:", absolute_error)

if squared_error > absolute_error:
    print("Squared error penalizes large errors more (sensitive to outliers).")
else:
    print("Absolute error is more robust to noise.")