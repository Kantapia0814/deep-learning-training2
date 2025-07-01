# 3.6 손글씨 숫자 인식
import numpy as np
import sys, os
import pickle
import chap3_2
import chap3_5
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image

# 3.6.1 MNIST 데이터셋
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

'''print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)'''

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,)
img = img.reshape(28, 28)  
print(img.shape)  # (28, 28)

img_show(img)

# 3.6.2 신경망의 추론 처리
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = chap3_2.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = chap3_2.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = chap3_5.softmax(a3)

    return y

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))