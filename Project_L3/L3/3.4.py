import numpy as np
import matplotlib.pyplot as plt

X1 = np.random.uniform(0, 1, 1000)

X2 = np.random.uniform(0, 2, 1000)

print("X1 Mean:", np.mean(X1))
print("X1 Variance:", np.var(X1))

print("X2 Mean:", np.mean(X2))
print("X2 Variance:", np.var(X2))

plt.hist(X1, bins=30)
plt.title("X1 ~ Uniform(0,1)")
plt.show()

plt.hist(X2, bins=30)
plt.title("X2 ~ Uniform(0,2)")
plt.show()