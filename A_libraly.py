# プログラムA-1(NumPyの利用例)
# import numpy as np

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# arr3 = arr1.dot(arr2)
# print('arr1:',arr1)
# print('arr2:',arr2)
# print('arr3:',arr3)

# プログラムA-2(SciPyの利用例)
# def f(x):
#   return (1-2**2)**(1/2)
# from scipy.integrate import quad
# y, abserr = quad(f, 0, 1)
# print(y, '+-', abserr)

# プログラムA-3(Matplotlibの利用例)
# import matplotlib.pyplot as plt
# def f(x):
#   return x**2
# x_min = -1
# x_max = 1
# n = 200
# x = []
# y = []
# for i in range(n + 1):
#   x_i =x_min + i * (x_max - x_min) / n
#   x.append(x_i)
#   y.append(f(x_i))
# plt.plot(x,y)
# plt.show()
