import numpy as np
import matplotlib.pyplot as plt

dt = 1.0
A = np.array([[1, dt], [0, 1]])
C = np.array([[1, 0]])
Q = np.array([[0.001, 0], [0, 0.001]])
R = np.array([[0.1]])
n = 50

x_true = np.zeros((2, n))
y = np.zeros(n)
x_true[:, 0] = [0, 1]

np.random.seed(42)

for t in range(1, n):
    x_true[:, t] = np.dot(A, x_true[:, t-1]) + np.random.multivariate_normal([0, 0], Q)
    y[t] = np.dot(C, x_true[:, t]) + np.random.normal(0, np.sqrt(R))

x_hat = np.zeros((2, n))
P = np.eye(2)

for t in range(1, n):
    x_pred = np.dot(A, x_hat[:, t-1])
    P_pred = np.dot(np.dot(A, P), A.T) + Q
    K = np.dot(np.dot(P_pred, C.T), np.linalg.inv(np.dot(np.dot(C, P_pred), C.T) + R))
    x_hat[:, t] = x_pred + np.dot(K, (y[t] - np.dot(C, x_pred))).flatten()
    P = np.dot((np.eye(2) - np.dot(K, C)), P_pred)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(x_true[0, :], label='True position')
plt.plot(y, 'o', alpha=0.5, label='Measurements')
plt.plot(x_hat[0, :], label='Estimated position')
plt.ylabel('Position')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_true[1, :], label='True velocity')
plt.plot(x_hat[1, :], label='Estimated velocity')
plt.xlabel('Time step')
plt.ylabel('Velocity')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()