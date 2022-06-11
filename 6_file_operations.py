# プログラム6-1(ファイルの読み込み)
# f = open("test.txt", 'r', encoding='UTF-8')
# l = f.readline()
# while l:
#   print(l)
#   l = f.readline()
# f.close()

# プログラム6-2(ファイルの書き込み)
# f = open("test.txt", 'w', encoding='UTF-8')
# for i in range(10):
#   f.write(str(i) + "\n")
# f.close()

# プログラム6-3(CSVファイルの読み込み)
# rows = []
# f = open('subject.csv', 'r', encoding='UTF_8')
# l = f.readline()
# while l:
#   fixed_1 = l.rstrip()
#   rows.append(fixed_1.split(','))
#   l = f.readline()
# for i in rows:
#   print(i)

# プログラム6-4(ファイルの書き込み)
# f = open("power.csv", 'w', encoding='UTF-8')
# for i in range(10):
#   f.write(str(i) + ',' + str(i**2) + ',' + str(i**3) + '\n')
# f.close()