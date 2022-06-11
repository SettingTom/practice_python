# プログラム7-1(素数判定のプログラム)
# def isPrime(n):
#   if n < 2:
#     return False
#   for i in range(2, n):
#     if n % i == 0:
#       return False
#   return True
# p = int(input("input number:"))
# if isPrime(p):
#   print("素数である")
# else:
#   print("素数でない")

# プログラム7-2(素数判定のプログラム(改良版))
# import math

# def isPrime(n):
#   for i in range(2, int(math.sqrt(n) + 1)):
#     if n % i == 0:
#       return False
#   return True
# p = int(input("input number:"))
# if isPrime(p):
#   print("素数である")
# else:
#   print("素数でない")

# プログラム7-3(エラトステネスのふるいのプログラム)
# import math
# n = 1000
# primes = []
# numbers = range(2, n)
# sqrt_n = math.sqrt(n)
# while numbers[0] <= sqrt_n:
#   primes.append(numbers[0])
#   numbers = [n for n in numbers if n % numbers[0] != 0]
# print(primes + numbers)

# 7.1節末問題
# 問1.入力された自然数が素数かどうかを判定し、素数でない場合にはその数を割り切れる2以上の最小の自然数を表示せよ。
# 問2.100以上の素数を小さい方から順に20個求めて表示せよ。
# 問3.引数として与えられた自然数nが完全数かどうかを調べて返す関数isPerfect(n)を作成し、小さい方から完全数を3つ求めて表示せよ。
# 問4.引数で与えられた自然数より小さい素数の個数を返す関数numOfPrime(n)を定義し、2から100までの素数の数を表示せよ。

# 問1.解答
# import math
# def isPrime(n):
#   for i in range(2, int(math.sqrt(n) + 1)):
#     if n % i == 0:
#       return False
#   return True
# def isPrime2(n):
#   for j in range(2, int(math.sqrt(n) + 1)):
#     if n % j == 0:
#       print(j)
# p = int(input("input number:"))
# if isPrime(p):
#   print("素数である")
# else:
#   print("素数でない")
#   isPrime2(p)
# import math
# def minDivisor(n):
#   for i in range(2, int(math.sqrt(n) + 1)):
#     if n % i == 0:
#       return i
#   return 0
# P = int(input("input number:"))
# P_divisor = minDivisor(P)
# if P_divisor != 0:
#   print(P_divisor)

# 問2.解答
# import math
# def isPrime(n):
#   for i in range(2, int(math.sqrt(n) + 1)):
#     if n % i == 0:
#       return False
#     return True
# count = 0
# n = 100
# while count < 20:
#   if isPrime(n):
#     print(n)
#     count += 1
#   n += 1 

# 問3.解答
# def isPerfect(n):
#   m = 0
#   for i in range(1, n):
#     if n % i == 0:
#       m += i
#   if n == m:
#     return True
#   return False

# n = 2
# count = 0
# while count < 3:
#   if isPerfect(n):
#     print(n)
#     count += 1
#   n += 1

# 問4.解答
# import math
# def isPrime(n):
#   for i in range(2, int(math.sqrt(n) + 1)):
#     if n % i == 0:
#       return False
#   return True

# def numOfPrime(n):
#   count = 0
#   for i in range(2,n):
#     if isPrime(i):
#       count += 1
#   return count

# for i in range(2, 101):
#   print(str(i) + 'より小さい素数は' + str(numOfPrime(i)) + '個')

# プログラム7-4(因数分解のプログラム)
# n = int(input("input number="))
# p = 2
# factor = []
# while n > 1:
#   while n % p == 0:
#     factor.append(p)
#     n = n//p
#   p += 1
# print(factor)

# 7.2節末問題
# 問1.入力した自然数の、最大の素因数を求めて表示せよ。
# 問1.解答
# n = int(input("input number="))
# p = 2
# factor = []
# while n > 1:
#   while n % p == 0:
#     factor.append(p)
#     n = n//p
#   p += 1
# print(max(factor))
# def maxPrimeFactor(n):
#   for i in range(2, n):
#     while n % i == 0:
#       factor = i
#       n = n//i
#   return factor
# n = int(input("input number="))
# print(maxPrimeFactor(n))

# プログラム7-5(最大公約数を求めるプログラム)
# a = int(input("input a="))
# b = int(input("input b="))
# if a < b:
#   divisor = a
# else:
#   divisor = b
# while divisor > 1:
#   if a % divisor == 0 and b % divisor == 0:
#     break
#   divisor -= 1
# print("最大公約数は"+str(divisor))

# プログラム7-6(ユークリッドの互除法)
# a = int(input("input a="))
# b = int(input("input b="))
# while True:
#   r = a % b
#   if r == 0:
#     break
#   a = b
#   b = r
# print("最大公約数は"+str(b))

# 7.3節末問題
# 問1.ユークリッドの互除法のプログラミングにおいて、繰り返し処理の中で変数a,bの値を出力することにより、
# それぞれの値の変化の様子を確認できるように改良せよ。
# 問2.四つの値a,b,c,dを入力すると、a/b + c/dの計算結果を既約分数で表したときの分子と分母を表示せよ。
# ヒント：既約分数を求めるには元の分数の分子と分母をそれぞれ、分子と分母の最大公約数で割ればよい。

# 問1.解答
# a = int(input("input a="))
# b = int(input("input b="))
# while True:
#   r = a % b
#   if r == 0:
#     break
#   a = b
#   print("a="+str(a))
#   b = r
#   print("b="+str(b))
# print("最大公約数は"+str(b))

# 問2.解答
def maxDivisor(a,b):
  while True:
    r = a % b
    if r == 0:
      break
    a = b
    b = r
  return b

a = int(input("input a="))
b = int(input("input b="))
c = int(input("input c="))
d = int(input("input d="))

top = a*d + c*b
down = b*d
divisor = maxDivisor(top, down)

top /= divisor
down /= divisor

print("分子は" + str(top) + "分母は" + str(down))