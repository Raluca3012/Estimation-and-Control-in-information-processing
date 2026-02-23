import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 50
t = np.arange(N)
x0 = 0
x = np.zeros(N)
x[0] = x0
for k in range(N - 1):
    x[k+1] = x[k] + 1
noise = np.random.normal(0, 2, N)
y = x + noise

plt.figure()
plt.plot(t, x, linewidth=2)
plt.scatter(t, y, alpha=0.7)
plt.xlabel("Time step k")
plt.ylabel("Value")
plt.title("True State vs Noisy Observations")
plt.legend()
plt.grid()
plt.show()