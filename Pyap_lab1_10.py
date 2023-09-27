import math

s = 0
print("Enter N please:")

N = int(input())

for k in range(1, N + 1):
    s += (-1) ** k * math.factorial(2 * k + 1)

print(s)
