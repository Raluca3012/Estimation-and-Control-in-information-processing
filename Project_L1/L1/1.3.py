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

W = 5  
x_hat = np.zeros(N)

for k in range(N):
    start = max(0, k - W + 1)
    x_hat[k] = np.mean(y[start:k+1])

plt.figure()
plt.plot(t, x, label="True state x(k)", linewidth=2)
plt.scatter(t, y, label="Noisy observations y(k)", alpha=0.7)
plt.plot(t, x_hat, label=f"Moving average estimate (W={W})", linewidth=2)
plt.xlabel("Time step k")
plt.ylabel("Value")
plt.title("True vs Noisy vs Estimated (Moving Average)")
plt.grid()
plt.legend()
plt.show()