# プログラム9-1(ベクトルの和)
# def v_plus(v1,v2):
#   v = []
#   for i in range(len(v1)):
#     v.append(v1[i] + v2[i])
#   return v
# v = [1,2,3,4]
# u = [5,6,7,8]
# print(v_plus(v,u))

# プログラム9-2(ベクトルの内積)
# def in_product(v1,v2):
#   p = 0
#   for i in range(len(v1)):
#     p += v1[i] * v2[i]
#   return p
# v = [1,2,3,4]
# u = [5,6,7,8]
# print(in_product(v,u))

# 9.1節末問題
# 問1.二つのベクトルの差を計算して返す関数を定義して、v1=(10,4,5),v2=(2,6,11)のとき、
# v1-v2を求めて表示せよ。
# 問2.第一引数にスカラー値、第二引数にベクトルを表すリストを与えるとベクトルのスカラー値を計算して返す関数を定義して
# v1=(10,18)の3倍の値を求めて表示せよ。

# 問1.解答
# def v_minus(v1,v2):
#   v = []
#   for i in range(len(v1)):
#     v.append(v1[i] - v2[i])
#   return v
# v = [10, 4,5]
# u = [2,6,11]
# print(v_minus(v,u))

# # 問2.解答
# def v_multiple(n,v1):
#   v = []
#   for i in range(len(v1)):
#     v.append(v1[i] * n)
#   return v
# v1 = [10, 18]
# print(v_multiple(3,v1))

# プログラム9-3(行列の和)
# def m_plus(m1,m2):
#   m = []
#   for i in range(len(m1)):
#     r = []
#     for j in range(len(m1[0])):
#       r.append(m1[i][j] + m2[i][j])
#     m.append(r)
#   return m
# A = [[1,2],[3,4]]
# B = [[5,6],[7,8]]
# print(m_plus(A,B))

# プログラム9-4(行列の積)
# def m_product(m1,m2):
#   m = []
#   for i in range(len(m1)):
#     r = []
#     for j in range(len(m2[0])):
#       v = 0
#       for k in range(len(m2)):
#         v += m1[i][k] * m2[k][j]
#       r.append(v)
#     m.append(r)
#   return m
# m1 = [[1,2],[3,4]]
# m2 = [[5,6],[7,8]]
# print(m_product(m1,m2))

# 9章 章末問題
# [1]同じ次数の二つのベクトルの距離を求めて返す関数を作成し、次のベクトル間の距離を求めよ。
# v1=(6,-2,5,7), v2=(-5,2,5,-2)
# [2]引数に正方行列を指定すると、その転置行列を返す関数を作成し、次の行列の転置行列を表示せよ。
# A = [[1,2],[3,4]]
# [3]引数に自然数nを指定するとn×nの単位行列Eを返す関数を作成し、任意のn×n行列Mに対してME=Mであることを確認せよ。

# [1].解答
# import math
# def v_distance(v1,v2):
#   d = 0
#   for i in range(len(v1)):
#     d += (v1[i] - v2[i])**2
#     return math.sqrt(d)
# v1 = [6,-2,5,7]
# v2 = [-5,2,5,-2]
# print(v_distance(v1,v2))

# [2].解答
# def m_trans(m1):
#   m = []
#   for i in range(len(m1[0])):
#     v = []
#     for j in range(len(m1)):
#       v.append(m1[j][i])
#     m.append(v)
#   return m
# A = [[1,2],[3,4]]
# print(m_trans(A))

# [3].解答
# def m_product(m1,m2):
#   m = []
#   for i in range(len(m1)):
#     r = []
#     for j in range(len(m2[0])):
#       v = 0
#       for k in range(len(m2)):
#         v += m1[i][k] * m2[k][j]
#       r.append(v)
#     m.append(r)
#   return m
# def m_unit(n):
#   m = []
#   for i in range(n):
#     v = []
#     for j in range(n):
#       if i == j:
#         v.append(1)
#       else:
#         v.append(0)
#     m.append(v)
#   return m
# M = [[1,2],[3,4]]
# E = m_unit(3)
# print(m_product(M,E))