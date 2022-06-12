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