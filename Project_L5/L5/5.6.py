import numpy as np
import matplotlib.pyplot as plt

A = 1
C = 1
R = 0.5
n = 50

np.random.seed(42)

x_true = np.zeros(n)
y = np.zeros(n)
for t in range(1, n):
    x_true[t] = A * x_true[t-1] + np.random.normal(0, np.sqrt(0.01))
    y[t] = C * x_true[t] + np.random.normal(0, np.sqrt(R))

Q_values = [0.0001, 0.01, 1.0]
estimates = {}

for Q in Q_values:
    x_hat, P = 0.0, 1.0
    x_est = np.zeros(n)
    
    for t in range(1, n):
    
        x_pred = A * x_hat
        P_pred = A * P * A + Q
        
        K = P_pred * C / (C * P_pred * C + R)
        
        x_hat = x_pred + K * (y[t] - C * x_pred)
        P = (1 - K * C) * P_pred
        
        x_est[t] = x_hat
    
    estimates[Q] = x_est

plt.figure(figsize=(10,6))
plt.plot(x_true, 'k-', label='True state')
plt.plot(y, 'o', alpha=0.4, label='Measurements')

for Q in Q_values:
    plt.plot(estimates[Q], label=f'Estimate (Q={Q})')

plt.legend()
plt.title('Effect of Process Noise Covariance Q')
plt.xlabel('Time')
plt.ylabel('State')
plt.grid()
plt.show()

# Ex 7.
R_values = [0.01, 0.5, 5.0]
Q = 0.01
estimates_R = {}

for R in R_values:
    x_hat, P = 0.0, 1.0
    x_est = np.zeros(n)
    
    for t in range(1, n):
        x_pred = A * x_hat
        P_pred = A * P * A + Q
        K = P_pred * C / (C * P_pred * C + R)
        x_hat = x_pred + K * (y[t] - C * x_pred)
        P = (1 - K * C) * P_pred
        x_est[t] = x_hat
    
    estimates_R[R] = x_est

plt.figure(figsize=(10,6))
plt.plot(x_true, 'k-', label='True state')
plt.plot(y, 'o', alpha=0.4, label='Measurements')

for R in R_values:
    plt.plot(estimates_R[R], label=f'Estimate (R={R})')

plt.legend()
plt.title('Effect of Measurement Noise Covariance R')
plt.xlabel('Time')
plt.ylabel('State')
plt.grid()
plt.show()