import numpy as np

size1 = 12
size2 = 12

arr = [[0] * size1 for i in range(size2)]

for i in range(size1):
    for j in range(size2):
        arr[i][j]=j+1
        if i>j:
            arr[i][j]=0


print(np.matrix(arr))