def partition_index(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] >= pivot:
            end -= 1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]
    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

    return end


def quick_sort(a, start, end):
    if start < end:
        pi = partition_index(a, start, end)
        quick_sort(a, start, pi - 1)
        quick_sort(a, pi + 1, end)


if __name__ == '__main__':
    a = [11, 9, 29, 7, 2, 15, 28]
    print("Before sort: ", a)
    quick_sort(a, 0, len(a) - 1)
    print("After sort: ", a)
