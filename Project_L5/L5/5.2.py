import numpy as np
import matplotlib.pyplot as plt

A = 1.05
B = 1.0   
T = 10    

u = np.ones(T)

true_x = np.zeros(T + 1)  
pred_x = np.zeros(T + 1)  

true_x[0] = 10.0
pred_x[0] = 0.0  

for t in range(1, T + 1):
    true_x[t] = A * true_x[t-1] + B * u[t-1]

for t in range(1, T + 1):
    pred_x[t] = A * pred_x[t-1] + B * u[t-1] 

time_steps = np.arange(0, T + 1)

plt.figure(figsize=(10, 6))
plt.plot(time_steps, true_x, 'b-', label='True State', linewidth=2, marker='o')
plt.plot(time_steps, pred_x, 'r--', label='Predicted State (from x_hat(0|0)=0)', linewidth=2, marker='s')
plt.xlabel('Time Step (t)')
plt.ylabel('State Value x(t)')
plt.title('True State vs Predicted State (Prediction Step Only)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
