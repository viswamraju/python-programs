def rotate_array(arr, n):
    size = len(arr)
    temp = []

    for i in range(n):
        temp.append(arr[i])
    print(temp)
    i = 0
    for j in range(n, size):
        arr[i] = arr[j]
        i += 1

    for _ in range(n):
        arr[i] = temp[_]
        i += 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    print("Before Rotate: ", arr)
    rotate_array(arr, 2)
    print("After Rotate: ", arr)