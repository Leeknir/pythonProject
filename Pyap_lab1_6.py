import random

m, n = map(int, input("m n » ").split())
mminus = m - 1
nminus = n - 1
B = [[0.0] * n for _ in range(m)]
a = 0.0
max_val = -6.0

print("\nMatrix:")
for k in range(m):
    for l in range(n):
        B[k][l] = random.uniform(-5.0, 7.0)
        if B[k][l] > max_val:
            max_val = B[k][l]
            i = k
            j = l
        print("{:5.2f}".format(B[k][l]), end=" ")
    print()

'''if i != mminus:
    for l in range(n):
        a = B[i][l]
        B[i][l] = B[mminus][l]
        B[mminus][l] = a

if j != nminus:
    for k in range(m):
        a = B[k][j]
        B[k][j] = B[k][nminus]
        B[k][nminus] = a'''

temp = B[i][j]
B[i][j] = B[n-1][m-1]
B[n-1][m-1] = temp

print("\nMax = {:5.2f}".format(max_val))
print("\nTransformed Matrix:")
for k in range(m):
    for l in range(n):
        print("{:5.2f}".format(B[k][l]), end=" ")
    print()