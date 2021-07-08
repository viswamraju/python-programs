def sub(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Addition is not possible")
    else:

        result = [[j for j in range(len(mat1[0]))] for i in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                result[i][j] = mat1[i][j] - mat2[i][j]
        print(result)


if __name__ == '__main__':
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    mat2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]
    sub(mat1, mat2)
