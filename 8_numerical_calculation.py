# プログラム8-1(√3を二分法で求めるプログラム)
# def f(x):
#   return x**2 - 3
# a = 1
# b = 2
# eps = 0.000001
# while b - a > eps:
#   c = (a+b)/2
#   if f(c) < 0:
#     a = c
#   else:
#     b = c
# print(c)

# プログラム8-2(√二分法の収束を調べる)
# def f(x):
#   return x**2 - 3
# file = open("bisection_root3.csv", 'w', encoding='UTF-8')
# a = 1
# b = 2
# for i in range(50):
#   c = (a+b)/2
#   if f(c) < 0:
#     a = c
#   else:
#     b = c
#   file.write(str(i+1) + ',' + str(c) + '\n')
# file.close()

# プログラム8-3(√3をニュートン法で求めるプログラム)
# import math
# def f(x):
#   return x**2 - 3
# def df(x):
#   return 2*x
# def nextX(x):
#   return x - (f(x)/df(x))

# x0 = 2
# x1 = nextX(x0)
# eps = 0.000001
# while math.fabs(x0-x1) > eps:
#   x0 = x1
#   x1 = nextX(x1)
# print(x1)

# プログラム8-4(ニュートン法の収束を調べる)
# import math
# def f(x):
#   return x**2 - 3
# def df(x):
#   return 2*x
# def nextX(x):
#   return x - (f(x)/df(x))

# file = open("newton_root3.csv", 'w', encoding='UTF-8')
# x0 = 2
# x1 = nextX(x0)
# for i in range(50):
#   x0 = x1
#   x1 = nextX(x1)
#   file.write(str(i+1) + ',' + str(x1) + '\n')
# file.close

# 8.1節末問題
# 問1.√3の値を求める問題において、二分法とニュートン法の収束の速さを比較するために、
# 繰り返し回数と二分法の近似値、ニュートンの近似値を同時にCSVファイルに書き出せ。
# 問2.一般に五次以上の方程式において代数的な解法は存在しない。しかし、二分法やニュートン法で解を近似的に求めることができることを
# 次の方程式をニュートン法で求め確認せよ。
# 2x^5 - 3x^4 - 6x^ - 99 = 0

# 問1.解答
# import math
# def f(x):
#   return x**2 - 3
# def df(x):
#   return 2*x
# def nextX(x):
#   return x - (f(x)/df(x))

# file = open("compare_root3.csv", 'w', encoding='UTF-8')
# a = 1
# b = 2
# x0 = 2
# x1 = nextX(x0)
# for i in range(50):
#   c = (a+b)/2
#   if f(c) < 0:
#     a = c
#   else:
#     b = c
#   x0 = x1
#   x1 = nextX(x1)
#   file.write(str(i+1) + ',' + str(c) + ',' + str(x1) + '\n')
# file.close

# 問2.解答
# import math
# def f(x):
#   return 2*x**5 - 3*x**4 - 6*x -99
# def df(x):
#   return 10*x**4 - 12*x**3 - 6
# def nextX(x):
#   return x - (f(x)/df(x))

# x0 = 2
# x1 = nextX(x0)
# eps = 0.000001
# while math.fabs(x0-x1) > eps:
#   x0 = x1
#   x1 = nextX(x1)
# print('x=' + str(x1) + ',f(x)=' + str(f(x1)))

# プログラム8-5(各点の値を取得)
# def f(x):
#   return x**2
# file = open("y_eq_x2.csv", 'w', encoding='UTF-8')
# x_min = -1
# x_max = 1
# n = 200
# dx = (x_max - x_min) / n
# for i in range(n+1):
#   x_i = x_min + i * dx
#   file.write(str(x_i) + ',' + str(f(x_i)) + '\n')
# file.close()

# プログラム8-6(各点の微分係数を計算)
# def f(x):
#   return x**2
# file = open("y_eq_x2_d.csv", 'w', encoding='UTF-8')
# x_min = -1
# x_max = 1
# n = 200
# dx = (x_max - x_min) / n
# for i in range(n+1):
#   x_i = x_min + i + dx
#   df = (f(x_i + dx) - f(x_i)) / dx
#   file.write(str(x_i) + ',' + str(f(x_i)) + ',' + str(df) + '\n')
# file.close()

# プログラム8-7(区分求積法のプログラム)
# def f(x):
#   return x**3 - 2 * x**2 + 2 * x +5
# a = 0
# b = 2
# n = 200
# inte = 0
# dx = (b - a)/n
# for i in range(n):
#   x_i = a + i * dx
#   inte += f(x_i) * dx
# print(inte)

# プログラム8-8(台形法のプログラム)
# def f(x):
#   return x**3 - 2 * x**2 + 2 * x +5
# a = 0
# b = 2
# n = 200
# inte = 0
# dx = (b - a)/n
# for i in range(n):
#   x_i = a + i * dx
#   inte += (f(x_i) + f(x_i + dx)) * dx / 2
# print(inte)

# プログラム8-9(モンテカルロ法のプログラム)
# import random
# def f(x):
#   return x**2 + 1
# a = -1
# b = 1
# h = 2
# n = 100000
# count = 0
# for i in range(n):
#   x = random.uniform(a,b)
#   y = random.uniform(0,h)
#   if y < f(x):
#     count += 1
# print('領域内の点の数:' + str(count) + '/' + str(n))
# print('解の近似値:' + str((count/n) * h * (b-a)))

# プログラム8-10(モンテカルロ法による円周率の計算)
# import random
# a = 0
# b = 1
# h = 1
# n = 100000
# count = 0
# for i in range(n):
#   x = random.uniform(a,b)
#   y = random.uniform(0,h)
#   if x**2 + y**2 < 1:
#     count += 1
# print('領域内の点の数:' + str(count) + '/' + str(n))
# print('積分値の近似値:' + str(count * h * (b-a) / n))
# print('円周率の近似値:' + str(count * h * (b-a) / n * 4))