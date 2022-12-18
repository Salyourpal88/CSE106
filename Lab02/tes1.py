import numpy as np

print("Problem 1:")
a = np.random.randint(low = 2, high = 11, size = (4,2)) #Number 2-10, 4 rown and 2 column matrix
print(a)
print('\n')

print("Problem 2:")
x = np.zeros((8,8), dtype = int)
x[::2,1::2] = 1 #(row 0 for every 2 rows, coulmn 1 for every 2 columns)
x[1::2,::2] = 1 #(row 1 for every 2 rows, coulmn 0 for every 2 columns)
print(x)
print('\n')

print("Problem 3:")
List = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
print(np.amax(List))
print(np.amin(List))
print('\n')

print("Problem 4:")
List = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
print(List[List > 35])
print('\n')

print("Problem 5:")
List = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
List = List*(9/5) + 32
print(List)
