# プログラム4-1(組込み関数absの使用例)
# result = abs(-170)
# print(result)
# print(abs(-8*7))

# プログラム4-2(数値を扱う組込み関数)
# print(abs(0.98))
# print(abs(-0.98))
# print(max(1,5,7,4))
# print(min(1,5,7,4))
# print(round(7.65))
# print(round(2.1))

# プログラム4-3(イテラブルを扱う組込み関数(1))
# for i in range(1,3):
#   print(i)
# list1 = [6,2,6,7,1,9]
# str1 = "athagja"
# print('list1の要素数は'+str(len(list1)))
# print('str1の文字数は'+str(len(str1)))
# print(sorted(list1))
# print(sorted(list1, reverse=True))
# print(sorted(str1))
# print(sorted(str1, reverse=True))
# print(sum(list1))

# プログラム4-4(イテラブルを扱う組込み関数(2))
# input1 = input('input number')
# print('入力された文字列は「' + input1 + '」')
# print('input1の型は'+str(type(input1)))
# input_number = int(input1)
# print('input_numberの型は'+str(type(input_number)))
# print('入力された値の2乗は'+str(input_number**2))

# プログラム4-5(mathモジュールの利用)
# import math
# y1 = math.factorial(7)
# y2 = math.log2(1024)
# y3 = math.sin(math.pi/2)
# print(y1)
# print(y2)
# print(y3)

# プログラム4-6(randomモジュールの利用)
# import random
# for i in range(5):
#   print(random.random())
# for j in range(5):
#   print(random.uniform(10,100))
# for k in range(5):
#   print(random.randint(1,6))

# プログラム4-7(関数の定義と利用)
# def suss(x):
#   return x + 1
# print(suss(3))

# プログラム4-8(返り値を返さない関数)
# def print_len_eo(s):
#   if len(s)%2==0:
#     print('偶数文字列')
#   else:
#     print('奇数文字列')
# print_len_eo('abcdef')
# print_len_eo('abc')

# プログラム4-9(ローカル変数を持つ関数)
# def inverse(x):
#   inversed_x = 1 / x
#   return inversed_x
# a = inverse(4)
# print(a)

# プログラム4-10(参照渡しと値渡しの比較)
# def changeIntTest(x):
#   x *= 2
# def changeListTest(x):
#   x[0] *= 2
# n = 5
# li = [5]
# changeIntTest(n)
# changeListTest(li)
# print(n)
# print(li[0])

# プログラム4-11(再起呼び出しによる階乗計算)
# def fact(n):
#   if n == 1:
#     return 1
#   return n * fact(n-1)
# print(fact(7))