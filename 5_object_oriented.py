# プログラム5-1(listメソッドの使用例)
# list1 = [6,2,4,3,6,1]
# print(list1.count(6))
# print(list1.count(5))
# print(list1.index(1))
# print(list1.index(6))
# list1.append(5)
# print(list1)
# list1.remove(6)
# print(list1)
# list1.pop()
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# プログラム5-2(辞書型メソッドの使用例)
# d = {'a':10,'b':20,'c':30,}
# d.pop('b')
# d.update({'c':100, 'd':200})
# print('全てのキーの表示')
# for k in d.keys():
#   print(k)
# print('全ての値の表示')
# for v in d.values():
#   print(v)
# print('全ての要素の表示')
# for i in d.items():
#   print(i)

# プログラム5-3(文字列メソッドの使用例)
# s = 'abcabc'
# print(s.find('bc'))
# print(s.count('bc'))
# sp = s.split('b')
# print(sp)

# プログラム5-4(クラスの定義と利用)
# import math

# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#   def get_distance(self, p):
#     return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
#   def get_midpoint(self, p):
#     return Point((self.x + p.x)/2, (self.y + p.y)/2)
# p1 = Point(5, 7)
# p2 = Point(2, 3)
# print(p1.get_distance(p2))
# mp = p1.get_midpoint(p2)
# print(str(mp.x) + ',' + str(mp.y))

# プログラム5-5(クラス変数の利用)
# import math

# class Point:
#   count = 0
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#     Point.count += 1
#     self.id = Point.count
#   def get_distance(self, p):
#     return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
#   def get_midpoint(self, p):
#     return Point((self.x + p.x)/2, (self.y + p.y)/2)
# p1 = Point(5, 7)
# p2 = Point(2, 3)
# p3 = Point(9, 6)
# print(p1.id)
# print(p2.id)
# print(p3.id)

# 5章 章末問題
# [1]初めに空リストnumbersを定義し、ユーザーから繰り返し自然数が入力されるたびに
# numbersにその自然数を格納していくプログラムを作成せよ。
# [2]三次元空間上の点を表すクラスPoint3Dを定義し、2点間の距離を計算するメソッドを定義せよ。
# また、そのクラスを用いて、2点(1,2,3), (4,5,6)間の距離を求めよ。

# numbers = []
# while True:
#   n = int(input('input number:'))
#   if n in numbers:
#     break
#   else:
#     numbers.append(n)
# print(numbers)

# import math

# class Point3D:
#   def __init__(self, x, y, z):
#     self.x = x
#     self.y = y
#     self.z = z
#   def get_distance(self, p):
#     return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2)
# p1 = Point3D(1, 2, 3)
# p2 = Point3D(4, 5, 6)
# print(p1.get_distance(p2))