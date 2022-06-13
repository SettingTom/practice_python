# プログラム10-1(三つの組み合わせ最適化)
# class Snack:
#   def __init__(self, name, price, like):
#     self.name = name
#     self.price = price
#     self.like = like

# sn1 = Snack("チョコ", 130, 18)
# sn2 = Snack("ポテトチップス", 120, 15)
# sn3 = Snack("クッキー", 80, 12)
# sn4 = Snack("ラムネ", 30, 4)
# sn5 = Snack("ガム", 20, 2)
# sn_set = {sn1, sn2, sn3, sn4, sn5}

# max_like = 0
# s1 = None
# s2 = None
# s3 = None
# for x1 in sn_set:
#   for x2 in sn_set:
#     for x3 in sn_set:
#       if x1.price + x2.price + x3.price > 300:
#         continue
#       if x1.like + x2.like + x3.like > max_like:
#         max_like = x1.like + x2.like + x3.like
#         s1 = x1
#         s2 = x2
#         s3 = x3
# print(s1.name + s2.name + s3.name)
# print("合計値:" + str(s1.price + s2.price + s3.price))
# print("総満足度:" + str(s1.like + s2.like + s3.like))