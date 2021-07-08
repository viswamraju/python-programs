
def make_list_flat(lst):
    flat_list = []
    for item in lst:
        flat_list.extend(item)
    print(flat_list)


def make_list_flat_1(lst):
    print([item for sublist in lst for item in sublist])


if __name__ == '__main__':
    nestedlist = [[1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
    # make_list_flat(nestedlist)
    # make_list_flat_1(nestedlist)
    print([1, 2, 3] + [4, 5, 6])

