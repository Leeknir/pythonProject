print("введите текст")
a = str(input())
a = a.replace(',', '')
a = a.split()
a = list(filter(lambda w: w[0] == w[-1], a))
a = len(a)
print(a)