import numpy as np

A = [[1, 1],
     [2, 1],
     [3, 1]]

y = [40, 42, 45]

x = np.array([1, 2, 3])
y = np.array([40, 42, 45])

A = np.vstack([x, np.ones(len(x))]).T

a, b = np.linalg.lstsq(A, y, rcond=None)[0]

print("a=", a,"b=", b)