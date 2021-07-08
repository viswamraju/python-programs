def binary_search(a, low, high, val):
    if high < low:
        return -1
    else:
        mid = (high + low) // 2

        if a[mid] == val:
            return mid
        elif val > a[mid]:
            return binary_search(a, mid + 1, high, val)
        else:
            return binary_search(a, low, mid - 1, val)


# def binary_search_iterative(a, val):
#     low = 0
#     high = len(a) - 1
#     found_index = -1
#     while high > low:
#         print("LOW:{}, HIGH:{}".format(low, high))
#         mid = (low + high) // 2
#         if a[mid] == val:
#             found_index = mid
#             break
#         elif val > a[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return found_index


if __name__ == '__main__':
    a = [2, 3, 4, 10, 40]
    # print(binary_search(a, 0, len(a)-1, 11))
    # print(binary_search_iterative(a, 10))

