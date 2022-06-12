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