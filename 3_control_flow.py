# プログラム3-1(if文の使用例(1))
# x=55
# if x >= 10 and x < 100:
#   print(x)
# print('実行終了')

# プログラム3-2(if文の使用例(2))
# n=16
# m=11
# if n > m:
#   print(n)
# elif n < m:
#   print(m)
# else:
#   print('等しい値です')

# プログラム3-3(if文の入れ子構造例)
# a=8
# b=1
# c=6
# if a <= b:
#   if b <= c:
#     print(c)
#   else:
#     print(b)
# else:
#   if a <= c:
#     print(c)
#   else:
#     print(a)

# 3.1節末問題
# 問１.変数nを適当な自然数とし、nが偶数か奇数か判別せよ。
# 問２.変数nを適当な自然数とし、2で割り切れるが3で割り切れない場合は2を、
    # 3で割り切れるが2で割り切れない場合は3を、
    # 2でも3でも割り切れる場合は2と3を表示せよ。
    # 2でも3でも割り切れない場合は何も表示しない。
# n=6
# if n % 2 == 0:
#   print("偶数です")
# else:
#   print("奇数です")

# if n % 2 == 0 and n % 3 == 0:
#   print(2, 3)
# elif n % 2 == 0:
#   print(2)
# elif n % 3 == 0:
#   print(3)

# プログラム3-4(while文の例)
# i=0
# while i < 5:
#   print(i)
#   i += 1

# プログラム3-4(while文の例)
# total=0
# n=0
# while total <= 10000:
#   n += 1
#   total += n
# print("10000を超える最小のnは"+str(n))
# print("そのときの合計値は"+str(total))