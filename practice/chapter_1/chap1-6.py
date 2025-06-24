import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 1.6.1 단순한 그래프 그리기
'''x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()'''

# 1.6.2 pyplot의 기능
'''x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")    # cos 함수는 점선으로 그리기
plt.xlabel("x")         # x축 이름
plt.ylabel("y")         # y축 이름
plt.title("sin & cos")  # 제목
plt.legend()            # 범례 출력
plt.show()'''

# 1.6.3 이미지 표시하기
img = imread('테스트 모델_1.png')
plt.imshow(img)         # 이미지를 '추가만'하는 함수
plt.show()              # '화면에 출력'하는 함수