import numpy as np

x = np.random.randint(1, 7, 1000)

A = (x % 2 == 0)      
B = (x >= 4)          

P_A_given_B = np.sum(A & B) / np.sum(B)

print("Estimated P(A|B):", P_A_given_B)