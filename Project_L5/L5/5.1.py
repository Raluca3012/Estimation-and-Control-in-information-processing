import numpy as np
import matplotlib.pyplot as plt
# 1. 
A = 1
B = 1
C = 1
u = 1           
time_steps = 30  

sigma_w = 0.5   
sigma_v = 1.0    

x = np.zeros(time_steps)
y = np.zeros(time_steps)

x[0] = 0

np.random.seed(42)

w = np.random.normal(0, sigma_w, time_steps)
v = np.random.normal(0, sigma_v, time_steps)

# 2. 
for t in range(time_steps):
    y[t] = C * x[t] + v[t]
    if t < time_steps - 1:
        x[t+1] = A * x[t] + B * u + w[t]

# 3. 
plt.figure(figsize=(10, 6))
plt.plot(range(time_steps), x, label='True State $$x(t)$$', marker='o', linestyle='-', color='blue')
plt.plot(range(time_steps), y, label='Measured Output $$y(t)$$', marker='x', linestyle='--', color='red')

plt.title('Simple Linear Dynamic System')
plt.xlabel('Time Step (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.show()