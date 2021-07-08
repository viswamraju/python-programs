def remove_ith_character(test_str, index):
    size = len(test_str)
    new_str = ""
    for i in range(size):
        if i != index:
            new_str += test_str[i]
    return new_str


if __name__ == '__main__':
    test_str = "GeeksForGeeks"
    print(remove_ith_character(test_str, 2))