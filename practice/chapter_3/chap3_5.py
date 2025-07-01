import numpy as np

# 3.5.1 항등 함수와 소프트맥스 함수 구현하기

'''a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)
sum_exp_a = np.sum(exp_a)
print(sum_exp_a)
y = exp_a / sum_exp_a
print(y)'''

'''def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y'''

def softmax(a):
    c = np.max(a)       
    exp_a = np.exp(a - c)       # 가장 큰 값을 빼면 지수가 전부 1 이하로 안정화됨
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))