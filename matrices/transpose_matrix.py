def transpose_matrix(mat1):
    result = [[mat1[j][i] for j in range(len(mat1))] for i in range(len(mat1[0]))]
    print(result)


if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4], [5, 6]]
    transpose_matrix(mat1)
