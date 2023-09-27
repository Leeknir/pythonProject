import math


def function(x):
    return math.sin(x) + (math.sin(x ** 2)) ** 2 + (math.sin(x ** 3)) ** 3


flag = 1
print("enter x, where x>=0.0 and x<=1.2")

while True:

    x = float(input())
    if (x >= 0.0) and (x <= 1.2):
        print(function(x))
        break  # Можно без него, тогда бесконечно будет запрашивать числа

    else:
        print("Wrong x")
        continue
