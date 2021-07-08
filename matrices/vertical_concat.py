def vertical_concat(mat1):
    tmp_list = []
    for i in range(len(mat1)):
        tmp_list.append(" ".join([sub[i] for sub in mat1]))
    print(tmp_list)


if __name__ == '__main__':
    mat1 = [["Gfg", "good"], ["is", "for"]]
    vertical_concat(mat1)