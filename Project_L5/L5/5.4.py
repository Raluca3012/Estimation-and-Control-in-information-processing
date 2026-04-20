import numpy as np
import matplotlib.pyplot as plt

A = 1          
B = 0          
C = 1          
Q = 0.01       
R = 0.5        
P = 1.0        
x_hat = 0.0    
n = 50         

true_x = np.zeros(n)
y = np.zeros(n)

np.random.seed(42)
for t in range(1, n):
    true_x[t] = A * true_x[t-1] + np.random.normal(0, np.sqrt(Q))
    y[t] = C * true_x[t] + np.random.normal(0, np.sqrt(R))

x_hat_vals = np.zeros(n)
P_vals = np.zeros(n)
K_vals = np.zeros(n)
innovation = np.zeros(n)

for t in range(1, n):
    x_hat_pred = A * x_hat
    P_pred = A * P * A + Q

    innovation[t] = y[t] - C * x_hat_pred

    K = P_pred * C / (C * P_pred * C + R)

    x_hat = x_hat_pred + K * innovation[t]
    P = (1 - K * C) * P_pred

    x_hat_vals[t] = x_hat
    P_vals[t] = P
    K_vals[t] = K

plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.plot(true_x, label='True State')
plt.plot(y, 'o', label='Measurement', alpha=0.5)
plt.plot(x_hat_vals, label='Kalman Estimate', linewidth=2)
plt.legend()
plt.title('Kalman Filter - State Estimation')

plt.subplot(3,1,2)
plt.plot(innovation, label='Innovation ν(t)')
plt.axhline(0, color='gray', linestyle='--')
plt.legend()
plt.title('Innovation over Time')

plt.subplot(3,1,3)
plt.plot(K_vals, label='Kalman Gain K(t)')
plt.plot(P_vals, label='Covariance P(t)')
plt.legend()
plt.xlabel('Time Step')
plt.title('Gain and Covariance')

plt.tight_layout()
plt.show()