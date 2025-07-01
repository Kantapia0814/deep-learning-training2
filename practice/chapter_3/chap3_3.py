import numpy as np

# 3.3.2 행렬의 곱
A = np.array([[1, 2], [3, 4]])
print(A.shape)
B = np.array([[5, 6], [7, 8]])
print(B.shape)
print(np.dot(A, B))

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.shape)
print(np.dot(A, B))
C = np.array([[1, 2], [3, 4]])
#print(np.dot(A, C))

# 3.3.3 신경망에서의 행렬의 곱
