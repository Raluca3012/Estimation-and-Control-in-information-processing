import numpy as np
import matplotlib.pyplot as plt

time = np.array([1, 2, 3, 4, 5])
energy = np.array([10, 12, 15, 18, 20])

A = np.vstack([time, np.ones(len(time))]).T
a, b = np.linalg.lstsq(A, energy, rcond=None)[0]

print("a (consumption rate) =", a)
print("b =", b)

energy_pred = a * time + b

plt.scatter(time, energy, label="Data")
plt.plot(time, energy_pred, label="Fitted line")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.legend()
plt.show()