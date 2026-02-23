import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

N = 50
t = np.arange(N)
x0 = 0
x = np.zeros(N)
x[0] = x0

for i in range(0, N-1):
    x[i+1] = x[i] + 1
    
plt.figure("Task 1 - Evolution of the true state"), plt.plot(t, x)
plt.xlabel("Time stamp"), plt.ylabel("State")
plt.grid(), plt.show()

