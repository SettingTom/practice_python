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
