import numpy as np

size1 = 5
size2 = 5
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr = [[0] * size1 for i in range(size2)]

for i in range(size1):
    for j in range(size2):
        arr[i][size1 - 1 - j] = arr[i][j] = j

    for i in range(size1):
        for j in range(size2):
            if arr[i][size1 - 1 - j] == arr[i][j]:
                b[i] = 1

# print(np.matrix(arr))
print(b)
