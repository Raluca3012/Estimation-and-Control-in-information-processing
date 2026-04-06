import numpy as np

sensor1 = np.array([1, 2])
sensor2 = np.array([2, 4])

A = np.column_stack((sensor1, sensor2))

print("A =\n", A)

rank = np.linalg.matrix_rank(A)
print("Rank =", rank)

if rank < A.shape[1]:
    print("Columns are linearly dependent")
    print("System fails because A^T A is singular")
else:
    print("Columns are independent")