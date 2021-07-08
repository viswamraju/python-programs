def remove_duplicates(lst):
    uniques = []
    for _ in lst:
        if _ not in uniques:
            uniques.append(_)

    print(uniques)


# Get new length, Inplace removal and no extra space
def remove_duplicates_1(lst):
    unique_pos = 1

    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            lst[unique_pos] = lst[i]
            unique_pos += 1
    print(unique_pos)


# Get array after deleting duplicates
def remove_duplicates_2(lst):
    unique_pos = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            lst[unique_pos] = lst[i]
            unique_pos += 1
    print(lst[:unique_pos])


if __name__ == '__main__':
    # lst = [1, 1, 2]
    # remove_duplicates(lst)
    # lst = [1, 1]
    # lst = [1, 1, 2]
    lst = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    remove_duplicates_2(lst)
