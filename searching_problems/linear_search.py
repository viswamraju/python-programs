def linear_search(a, val):
    found = -1
    for index, _val in enumerate(a):
        print(index, _val)
        if _val == val:
            found = index
            break
    return found


if __name__ == '__main__':
    a = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    print(linear_search(a, 100))
