def multiply(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("Matrix multiplication is not possible")

    else:

        result = [[0 for i in range(4)] for j in range(3)]
        print(result)

        comm = len(mat1[0])
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(comm):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        print(result)


if __name__ == '__main__':
    A = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]

    multiply(A, B)
