import numpy as np
import matplotlib.pyplot as plt

dt = 1.0
n = 50

A = np.array([[1, dt], [0, 1]])
B = np.array([[0.5 * dt**2], [dt]])
C = np.array([[1, 0]])
Q = np.array([[0.001, 0], [0, 0.001]])
R = np.array([[0.1]])
L = 0.5                       

x_true = np.zeros((2, n))       
x_hat = np.zeros((2, n))        
y = np.zeros(n)                 
u = np.zeros(n)                 

P = np.eye(2)                   

x_true[:, 0] = [5, 1]
x_hat[:, 0] = [0, 0]            

np.random.seed(42)

y[0] = np.dot(C, x_true[:, 0])[0] + np.random.normal(0, np.sqrt(R[0, 0]))

for k in range(1, n):
    u[k-1] = -L * (x_hat[0, k-1] + x_hat[1, k-1])

    process_noise = np.random.multivariate_normal([0, 0], Q)
    x_true[:, k] = np.dot(A, x_true[:, k-1]) + (B.flatten() * u[k-1]) + process_noise

    measurement_noise = np.random.normal(0, np.sqrt(R[0, 0]))
    y[k] = np.dot(C, x_true[:, k])[0] + measurement_noise

    x_pred = np.dot(A, x_hat[:, k-1]) + (B.flatten() * u[k-1])
    P_pred = np.dot(np.dot(A, P), A.T) + Q

    S = np.dot(np.dot(C, P_pred), C.T) + R
    K = np.dot(np.dot(P_pred, C.T), np.linalg.inv(S))

    innovation = y[k] - np.dot(C, x_pred)[0]
    x_hat[:, k] = x_pred + np.dot(K, np.array([[innovation]])).flatten()

    P = np.dot((np.eye(2) - np.dot(K, C)), P_pred)

u[n-1] = -L * (x_hat[0, n-1] + x_hat[1, n-1])

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(x_true[0, :], label='True position', linewidth=2)
plt.plot(x_hat[0, :], label='Estimated position', linewidth=2)
plt.plot(y, 'o', alpha=0.4, label='Measured position')
plt.ylabel('Position')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(x_true[1, :], label='True velocity', linewidth=2)
plt.plot(x_hat[1, :], label='Estimated velocity', linewidth=2)
plt.ylabel('Velocity')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(u, label='Control signal u(k)', linewidth=2)
plt.xlabel('Time step')
plt.ylabel('u(k)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()