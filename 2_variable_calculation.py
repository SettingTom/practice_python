# プログラム2-1(計算)
# print(4+7)
# print(16-9)

# プログラム2-2(コメント文の挿入)

# プログラム2-3(変数と計算)
# x = 10
# y = x + 5
# print(y)

# プログラム2-4(変数と型)
# n = 685
# r = 12.9
# c = 6 - 7j
# b = True
# s = "abc"
# z = 9.9 - 6 + 7j
# print(type(n))
# print(type(r))
# print(type(c))
# print(type(b))
# print(type(s))
# print(type(z))

# 2.2節末問題 
# BMI計算
# weight = 60
# height = 1.8
# BMI = weight/height**2
# print (BMI)

# プログラム2-5(文字列の連結)
# s1 = "こんにちは"
# s2 = "さようなら"
# print(s1 + s2)
# print(s1 * 3)
# s1 += s2
# print(s1)

# プログラム2-6(複数行の文字列)
# s = '''むかしむかしあるところに
# おじいさんとおばあさんが住んでいました。

# ある日おじいさんは山へ芝刈りに、おばあさんは川へ洗濯に行きました。
# '''
# print(s)

# プログラム2-7(文字列と数値の連結)
# n = 5
# m = 7
# print(str(n) + 'と' + str(m) + 'の和は' + str(n+m))

# 2.3節末問題
# BMI値を身長、体重と合わせて文章で表示せよ
# weight = 60
# height = 1.8
# print('身長'+str(height)+'m、'+'体重'+str(weight)+'kgの人のBMIは'+str(weight/height**2)+'です')

# プログラム2-8(リストの使い方)
# list1=[3, 5, 4, 10]
# list2=['abc', 1, 6.8]
# print(list1[0])
# print(list1[3])
# print(list2[0])
# print(list2[2])
# list1[3] = 100
# print(list1[3])
# print(list1)

# プログラム2-9(リストの使い方)
# li=[3.3, 5.5, 7.7]
# print(li[0])
# print(li[3])
# print(li[1])

# プログラム2-10(要素の追加・削除)
# li=['a', 'b', 'c']
# print('dを含むか:'+str('d' in li))
# li.append('d')
# print('dを含むか:'+str('d' in li))
# li.pop(3)
# print('dを含むか:'+str('d' in li))
# li.remove('a')
# print('aを含むか:'+str('a' in li))

# プログラム2-11(辞書の使い方)
# dict1={'鉛筆':60, '消しゴム':130,'定規':210,}
# print(dict1['鉛筆'])
# print(dict1['消しゴム'])
# print(dict1['定規'])

# プログラム2-12(辞書の使い方(表示の工夫))
# dict1={'鉛筆':60, '消しゴム':130,'定規':210,}
# print('鉛筆の値段は'+str(dict1['鉛筆'])+'円')
# print('消しゴムの値段は'+str(dict1['消しゴム'])+'円')
# print('定規の値段は'+str(dict1['定規'])+'円')

# プログラム2-13(辞書の要素の確認)
# student_name={101:'山田一郎', 102:'山田二郎'}
# print(103 in student_name)
# student_name[103] = '山田三郎'
# print(103 in student_name)
# print(student_name[103])

# プログラム2-14(タプルの定義)
# timetable={('月曜日', 1):'数学', ('月曜日', 2):'国語', ('火曜日', 1):'英語'}
# print('月曜日の２時限は'+timetable[('月曜日', 2)])

# プログラム2-15(集合の定義)
# set1={'a', 'b', 'c', 4, 5, 6}
# print('a' in set1)
# print('e' in set1)
# print(1 in set1)
# print(5 in set1)

# プログラム2-16(集合の演算)
# set1={1, 2, 3} | {4}
# set2={1, 2, 3} & {2, 3, 4}
# set3={1, 2, 3} - {2, 3}
# set4={1, 2, 3} ^ {2, 3, 4}
# print(1 in set1)
# print(4 in set1)
# print(2 in set2)
# print(4 in set2)
# print(1 in set3)
# print(2 in set3)
# print(1 in set4)
# print(2 in set4)