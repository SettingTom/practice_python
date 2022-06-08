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
    # print(a)

# 3.1節末問題
# 問1.変数nを適当な自然数とし、nが偶数か奇数か判別せよ。
# 問2.変数nを適当な自然数とし、2で割り切れるが3で割り切れない場合は2を、
#     3で割り切れるが2で割り切れない場合は3を、
#     2でも3でも割り切れる場合は2と3を表示せよ。
#     2でも3でも割り切れない場合は何も表示しない。
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

# プログラム3-5(合計値が10000を超える最小のn)
# total=0
# n=0
# while total <= 10000:
#   n += 1
#   total += n
# print("10000を超える最小のnは"+str(n))
# print("そのときの合計値は"+str(total))

# 3.2節末問題
# 問1.while文を用いて「hello world」を10回表示せよ。
# 問2.100までの7の倍数を全て表示せよ。
# 問3.2000より大きい(7*n)の最小のnを表示せよ。
# n=0
# s=0
# while n < 10:
#   print("hello wold")
#   n += 1

# while n < 100:
#   n += 1
#   if n % 7 == 0:
#     print(n)

# while 7 * n < 2000:
#   n += 1
# print(n)

# while s <= 2000:
#   n += 1
#   s += 7 * n
# print(n)

# プログラム3-6(for文の例)
# l = ["a", "b", "c", "d", "e"]
# for x in l:
#   print(x)

# プログラム3-7(等差数列の出力)
# for n in range(10):
#   print(3 * n + 7)

# プログラム3-8(リストの内包表記)
# l=[x**2 for x in range(5)]
# for x in l:
#   print(x)

# プログラム3-9(リストの内包表記(条件付))
# l=[x**2 for x in range(10) if x%2 != 0]
# print(l)

# プログラム3-10(九九の表)
# for x in range(1,10):
#   for y in range(1,10):
#     print(str(x)+"X"+str(y)+"="+str(x*y))

# プログラム3-11(5の倍数となる組合わせ)
# for n in range(1,7):
#   for m in range(1,7):
#     if (n + m) % 5 == 0:
#       print(str(n)+","+str(m))

# プログラム3-12(break文の例)
# count=0
# for n in range(100):
#   if n % 3 == 0 and n % 5 != 0:
#     count += 1
#     print(n)
#   if count >= 10:
#     break