def unique_values(test_dict):
    res = [{val for vals in list(test_dict.values()) for val in vals}]
    print(res)


if __name__ == '__main__':
    test_dict = {
        'gfg': [5, 6, 7, 8],
        'is': [10, 11, 7, 5],
        'best': [6, 12, 10, 8],
        'for': [1, 2, 5]
    }
    unique_values(test_dict)