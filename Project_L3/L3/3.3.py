import numpy as np

x = np.random.uniform(0, 1, 1000)
sample_mean = np.mean(x)
theoretical_mean = 0.5

print("Sample mean:", sample_mean)
print("Theoretical mean:", theoretical_mean)