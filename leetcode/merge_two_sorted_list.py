def merge_two_sorted_list(lst1, lst2):
    l = 0
    r = 0
    sorted_list = []
    while l < len(lst1) and r < len(lst2):
        if lst1[l] < lst2[r]:
            sorted_list.append(lst1[l])
            l += 1
        elif lst1[l] > lst2[r]:
            sorted_list.append(lst2[r])
            r += 1
        else:
            sorted_list.append(lst1[l])
            l += 1
            r += 1
    if lst1:
        sorted_list.extend(lst1[l:])
    if lst2:
        sorted_list.extend(lst2[r:])

    print(sorted_list)


if __name__ == '__main__':
    # lst1 = [1, 2, 4]
    # lst2 = [1, 3, 4]
    lst1 = [0]
    lst2 = [1]
    merge_two_sorted_list(lst1, lst2)