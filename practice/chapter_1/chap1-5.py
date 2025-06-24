import numpy as np

A = np.array([[1, 2], [3, 4]])
#print(A)
#print(A.shape)
#print(A.dtype)

B = np.array([[3, 0], [0, 6]])
#print(A + B)
#print(A * B)

# 1.5.6 원소 접근
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

for row in X:
    print(row)

X = X.flatten()         # X를 1차원 배열로 변환(평탄화)
print(X)
X[np.array([0, 2, 4])]  # 인덱스가 0, 2, 4인 원소 얻기

print(X > 15)
print(X[X>15])