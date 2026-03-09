# Use your simulation to point out at what value of r, the population
# the growth becomes chaotic. Show your result with a screenshot (PLOT THE DATA)

# Using the logistic map simulation, the behavior of the population was analyzed 
# for different values of the growth factor r
# From the bifurcation diagram, the population growth becomes chaotic at approximately r≈3.57.
# Before this value, the system shows stable or periodic oscillations, while 
# after this threshold the population values become irregular and highly 
# sensitive to initial conditions, indicating chaotic behavior.

import numpy as np
import matplotlib.pyplot as plt

r_values = np.linspace(2.5, 4.0, 5000)
x = np.full_like(r_values, 0.5)

for _ in range(1000):
    x = r_values * x * (1 - x)

rs = []
xs = []

for _ in range(200):
    x = r_values * x * (1 - x)
    rs.append(r_values.copy())
    xs.append(x.copy())

rs = np.array(rs).ravel()
xs = np.array(xs).ravel()

chaos_onset = 3.56995

plt.figure(figsize=(12, 7))
plt.plot(rs, xs, ',', alpha=0.35)
plt.axvline(chaos_onset, linestyle='--', linewidth=1.5, label=f'Chaos onset ≈ {chaos_onset}')
plt.xlabel('Growth factor r')
plt.ylabel('Long-term population values')
plt.title('Bifurcation Diagram of the Logistic Map')
plt.legend()
plt.grid(True)
plt.show()

