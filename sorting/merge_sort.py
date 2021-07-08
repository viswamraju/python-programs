def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(lst1, lst2):
    i = 0
    j = 0
    new_lst = list()
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            new_lst.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            new_lst.append(lst2[j])
            j += 1
        elif lst1[i] == lst2[j]:
            new_lst.extend([lst1[i], lst1[i]])
            i += 1
            j += 1

    while i < len(lst1):
        new_lst.append(lst1[i])
        i += 1

    while j < len(lst2):
        new_lst.append(lst2[j])
        j += 1
    return new_lst


if __name__ == '__main__':
    lst1 = [17, 21, 29, 38]
    lst2 = [4, 9, 25, 32]
    lst3 = [17, 4, 21, 9, 29, 25, 32, 38]
    # merge_two_sorted_lists(lst1, lst2)
    print(merge_sort(lst3))
