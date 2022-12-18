import numpy as np
from numpy import linalg

#Problem 1
print("Problem 1:")
A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[3, 1, 4],[2, 6, 1],[2, 9, 7]])
Answer1 = A + B
print(Answer1)
print('\n')

#Problem 2
print("Problem 2:")
Answer2 = A * B
print(Answer2)
print('\n')

#Problem 3
print("Problem 3:")
print(linalg.det(A))
print('\n')

#Problem 4
print("Problem 4:")
print(linalg.inv(A))
print('\n')

#Problem 5
print("Problem 5:")
print(linalg.eigvals(A))