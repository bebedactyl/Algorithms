def printMatrix(m):
    for row in m:
        print(row)


def parenStr(m, j, i):
    # This is the order in which the parenthesis should be placed.
    # print("First parenthesis after A" + str(traceback[0][-1]))
    # print("Second parenthesis after A" + str(traceback[0][2]) + " and A" + str(traceback[3][5]))
    # print('Third parenthesis after A' + str(traceback[1][2]) + ' and A' + str(traceback[3][4]))

    if j == i:

        print(chr(65 + j), end="")
        return
    else:
        print("(", end="")

        parenStr(m, m[j][i], i)

        parenStr(m, j, m[j][i] + 1)
        print(")", end="")


def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims) - 1
    m = [[None for i in range(n)] for j in range(n)]

    # Create the traceback table
    traceback = [[None for i in range(n)] for j in range(n)]

    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
    # print(m)

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2, n + 1):
        for i in range(n + 1 - chainLength):
            j = i + chainLength - 1

            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            # print(m)
            for k in range(i, j):

                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    traceback[i][j] = k
    # For traceback
    print('Traceback table:')
    for lst in traceback:
        print(lst)

    # Prints the optimal matrix and returns the optimal cost
    print("\nOptimal Matrix:")
    printMatrix(m)
    print("\nOptimal Cost:")
    print(m[0][n - 1])
    print("\nOptimal Parenthesis")
    parenStr(m, n - 1, 0)


dims = [30, 35, 15, 5, 10, 20, 25]
chainMatrix(dims)
