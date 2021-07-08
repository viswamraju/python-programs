def bubble_sort(lst):
    size = len(lst)
    for i in range(size - 1):
        for j in range(size-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(i, lst)


def bubble_sort_swaped(lst):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    print(lst)


if __name__ == '__main__':
    lst = [8, 3, 2, 4, 7, 1]
    # bubble_sort(lst)
    bubble_sort_swaped(lst)