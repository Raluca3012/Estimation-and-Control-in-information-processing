import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 50)
y = np.sin(0.2 * time) + 0.1 * np.random.randn(len(time))          
C_hat_pred = np.sin(0.2 * time) + 0.05 * np.random.randn(len(time)) 


innovation = y - C_hat_pred

plt.figure(figsize=(8,4))
plt.plot(time, innovation, marker='o', label='Innovation ν(t)')
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel('Time step t')
plt.ylabel('Innovation ν(t)')
plt.title('Innovation over Time')
plt.legend()
plt.grid(True)
plt.show()