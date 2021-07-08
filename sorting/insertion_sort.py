def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_ele = lst[i]

        # previous to i is sorted list
        j = i - 1

        # code to place current element in already sorted array
        while j >= 0 and current_ele < lst[j]:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = current_ele

    print(lst)


if __name__ == '__main__':
    lst = [8, 3, 2, 4, 7, 1]
    insertion_sort(lst)
