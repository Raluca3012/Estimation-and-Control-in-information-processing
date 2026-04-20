import numpy as np
import matplotlib.pyplot as plt

A = 1
B = 0
C = 1
Q = 0.01       
R = 0.5
n = 50
np.random.seed(42)

x_true = np.zeros(n)
y = np.zeros(n)
for t in range(1, n):
    x_true[t] = A * x_true[t-1] + np.random.normal(0, np.sqrt(Q))
    y[t] = C * x_true[t] + np.random.normal(0, np.sqrt(R))

x_pred = np.zeros(n)
for t in range(1, n):
    x_pred[t] = A * x_pred[t-1]  

mse_pred = np.mean((x_true - x_pred)**2)

x_hat = 0.0
P = 1.0
x_kalman = np.zeros(n)

for t in range(1, n):
    x_hat_pred = A * x_hat
    P_pred = A * P * A + Q

    K = P_pred * C / (C * P_pred * C + R)

    x_hat = x_hat_pred + K * (y[t] - C * x_hat_pred)
    P = (1 - K * C) * P_pred

    x_kalman[t] = x_hat

mse_kalman = np.mean((x_true - x_kalman)**2)

print(f"MSE (Prediction only): {mse_pred:.4f}")
print(f"MSE (Full Kalman filter): {mse_kalman:.4f}")

plt.figure(figsize=(10,5))
plt.plot(x_true, label='True state')
plt.plot(y, 'o', label='Measurements', alpha=0.5)
plt.plot(x_pred, '--', label='Prediction only')
plt.plot(x_kalman, label='Kalman estimate', linewidth=2)
plt.legend()
plt.title('Prediction Only vs Full Kalman Filter')
plt.xlabel('Time step')
plt.ylabel('State value')
plt.grid(True)
plt.show()