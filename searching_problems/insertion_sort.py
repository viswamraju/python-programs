"""

Assume first element is sorted so start from 1 to len(lst)

1. we need to ensure left part is sorted already
2. get current value and previous position
3. Keep on compare current element with left half.
4. Once we find current element is greater than element in left sorted array
then insert current element there
"""


def insertion_sort(a):
    for i in range(1, len(a)):
        current_element = a[i]

        j = i - 1

        while j >= 0 and a[j] > current_element:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = current_element


def insertion_sort_recursive(a, n):
    if n <= 1:
        return
    insertion_sort_recursive(a, n-1)

    last = a[n - 1]
    j = n - 2

    while j >= 0 and a[j] > last:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = last


if __name__ == '__main__':
    a = [12, 11, 13, 5, 6]
    print("Before sort: ", a)
    # insertion_sort(a)
    insertion_sort_recursive(a, len(a))
    print("After sort: ", a)
