def create_matrix(x, y):
    i = 0
    tmp_list1 = []
    for j in range(x):
        tmp_list2 = []
        for k in range(y):
            tmp_list2.append(i)
            i += 1
        tmp_list1.append(tmp_list2)
    print(tmp_list1)


def create_matrix_list_comp(x, y):
    a = [[j for j in range(y)] for i in range(x)]
    print(a)


if __name__ == '__main__':
    # create_matrix(3, 3)
    create_matrix_list_comp(3, 3)
