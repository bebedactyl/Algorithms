def printMatrix(m):
    for row in m:
        print(row)

def matrixMult(A, B):
    # number of rows of the first and the number of columns of the second matrix.
    dimA = len(A[0])
    dimB = len(B)

    if dimA == dimB:
        C = [[None for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                result = 0
                for k in range(len(B)):
                    result += A[i][k] * B[k][j]
                    C[i][j] = result
        return C
    else:
        print('Incorrect Dimensions')

# Testing code
# Test1
print('\nResults: Test 1')
A = [[2, -3, 3],
     [-2, 6, 5],
     [4, 7, 8]]
B = [[-1, 9, 1],
     [0, 6, 5],
     [3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test2
print('\nResults: Test 2')
A = [[2, -3, 3, 0],
     [-2, 6, 5, 1],
     [4, 7, 8, 2]]
B = [[-1, 9, 1],
     [0, 6, 5],
     [3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test3
print('\nResults: Test 3')
A = [[2, -3, 3, 5],
     [-2, 6, 5, -2]]
B = [[-1, 9, 1],
     [0, 6, 5],
     [3, 4, 7],
     [1, 2, 3]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

