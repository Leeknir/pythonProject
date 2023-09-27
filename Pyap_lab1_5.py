import math


def f(x):
    if (x < 0.3):
        return math.sin((math.pi / 8) + math.fabs(x))
    if x >= 0.3:
        return math.sin((x ** 2 * math.pi) / 2)


print("Enter x, where x>=-0.5 and x<=1.2")


while True:

    x = float(input())
    if (x >= -0.5) and (x <= 1.2):
        print(f(x))
        break  # Можно без него, тогда бесконечно будет запрашивать числа

    else:
        print("Wrong x")
        continue

