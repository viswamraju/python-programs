def selection_sort(lst):
    size = len(lst)

    for i in range(size):
        min = lst[i]
        min_idx = i
        for j in range(i+1, size):
            if lst[j] < min:
                min = lst[j]
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(lst)


if __name__ == '__main__':
    lst = [8, 3, 2, 4, 7, 1]
    selection_sort(lst)
