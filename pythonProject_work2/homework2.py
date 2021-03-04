import matplotlib.pyplot as plt
import numpy as np


def function(x):
    y = pow(((5 + 4 * np.cos(x)) / 4), 0.5) + pow(((5 - 4 * np.cos(x)) / 4), 0.5)
    return y


def d_function(x):
    dy = 0.5 * np.sin(x) * (pow((5 - 4 * np.cos(x)) / 4, -0.5) - pow((5 + 4 * np.cos(x)) / 4, -0.5))
    return dy


def gradinet_descent1(n, x, a):
    for i in range(n):
        x = x - a * d_function(x)
        x_list.append(x)
    print(x_list)
    plt.plot(x_list, label='x')
    plt.plot(function(x_list), label='y')
    plt.legend()
    # plt.show()


def gradinet_descent2(n, x, a):
    for i in range(n):
        x = x + a * d_function(x)
        x_list.append(x)
    print(x_list)
    plt.plot(x_list, label='x')
    plt.plot(function(x_list), label='y')
    plt.legend()
    # plt.show()


def origin_function_show():
    plt.plot(np.arange(-10, 10, 0.00001),function(np.arange(-10, 10, 0.00001)))
    plt.show()


origin_function_show()
print("-------------------第一部分--------------------")

x = 1
n = 100
a = 0.2
x_list = [x]
plt.subplot(221)
gradinet_descent1(n, x, a)

x = 2
n = 100
a = 0.2
x_list = [x]
plt.subplot(222)
gradinet_descent1(n, x, a)

x = 3
n = 100
a = 0.2
x_list = [x]
plt.subplot(223)
gradinet_descent1(n, x, a)

x = 4
n = 100
a = 0.2
x_list = [x]
plt.subplot(224)
gradinet_descent1(n, x, a)

plt.show()

print("-------------------第二部分--------------------")

x = 1
n = 100
a = 0.2
x_list = [x]
plt.subplot(221)
gradinet_descent2(n, x, a)

x = 1
n = 100
a = 0.5
x_list = [x]
plt.subplot(222)
gradinet_descent2(n, x, a)

x = 1
n = 100
a = 1
x_list = [x]
plt.subplot(223)
gradinet_descent2(n, x, a)

x = 1
n = 100
a = 5
x_list = [x]
plt.subplot(224)
gradinet_descent2(n, x, a)

plt.show()
