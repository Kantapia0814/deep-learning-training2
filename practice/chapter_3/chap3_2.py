import numpy as np
import matplotlib.pylab as plt

# 3.2.2 계단 함수 구현하기
'''def step_function(x):
    if x > 0:
        return 1
    else:
        return 0'''

# 3.2.3 계단 함수의 그래프
def step_function(x):
    y = x > 0
    return y.astype(int)        # Numpy 1.20 이후부터 np.int가 사용 중단됨
    
'''x = np.array([-1.0, 1.0, 2.0])
print(step_function(x))'''

'''x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)                  # x,y 데이터 점들을 선으로 연결해서 그래프를 그리는 함수
plt.ylim(-0.1, 1.1)
plt.show()'''

# 3.2.4 시그모이드 함수 구현하기
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

'''x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)'''

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)
plt.plot(x, y1)
plt.plot(x, y2, color='k', linestyle='--', linewidth=0.8, label="step")
plt.ylim(-0.1, 1.1)
plt.show()
