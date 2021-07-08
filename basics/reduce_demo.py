from functools import reduce


def calc_sum():
    my_list = [1, 2, 3, 4, 5]
    print(reduce(lambda a, b: a + b, my_list))


def find_max():
    my_list = [1, 2, 3, 4, 5]
    print(reduce(lambda a, b: a if a > b else b, my_list))


find_max()
