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