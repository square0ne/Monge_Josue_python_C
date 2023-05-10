A = ((1, 2, 3),
     (4, 5, 6))
B = ((-1,  0),
     (0, 1),
     (1, 1))
C = ()

for i in range(0, len(A)):
    row = ()
    for j in range(0, len(B[0])):
        sum = 0
        for n in range(0, len(A[i])):
            sum += A[i][n] * B[n][j]
        row += (sum, )
    C += (row, )

for x in C:
    print(x)

