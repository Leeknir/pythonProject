print('A B C F')

for A in range(0,2):
    for B in range(0,2):
        for C in range(0,2):
            f = (not(A + B ^ C)) + A

            print(A, B, C, bool(f))
