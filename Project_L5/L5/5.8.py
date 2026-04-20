import numpy as np
import matplotlib.pyplot as plt

A = 1
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

x_hat, P = 0.0, 1.0
P_pred_list = []  
P_upd_list = []   

for t in range(1, n):
    x_pred = A * x_hat
    P_pred = A * P * A + Q
    P_pred_list.append(P_pred)
    K = P_pred * C / (C * P_pred * C + R)
    x_hat = x_pred + K * (y[t] - C * x_pred)
    P = (1 - K * C) * P_pred
    P_upd_list.append(P)

plt.figure(figsize=(9,5))
plt.plot(P_pred_list, label='Predicted covariance P(t|t-1)')
plt.plot(P_upd_list, label='Updated covariance P(t|t)')
plt.title('Covariance Analysis in Kalman Filter')
plt.xlabel('Time step')
plt.ylabel('Covariance value')
plt.legend()
plt.grid(True)
plt.show()