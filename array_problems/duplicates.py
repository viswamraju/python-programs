def remove_duplicates1(lst):
    myset = set(lst)
    print(myset)


def remove_duplicates2(lst):
    uniques = []
    for _ in lst:
        if _ not in uniques:
            uniques.append(_)
    print(uniques)


def remove_duplicates_3(lst):
    uniques = []
    [uniques.append(_) for _ in lst if _ not in uniques]
    print(uniques)


if __name__ == '__main__':
    lst = [5, 10, 15, 20, 3, 15, 25, 20, 30, 10, 100]
    remove_duplicates_3(lst)
