def is_monotonic(arr):
    print(all([arr[i] > arr[i+1] for i in range(len(arr) - 1)])
          or all([arr[i] < arr[i+1] for i in range(len(arr) - 1)]))


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [6, 5, 8, 3, 2, 1]
    is_monotonic(arr2)
