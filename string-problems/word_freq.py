
def using_dict_comprehension(string):
    print({_: string.count(_) for _ in string.split()})


def using_dict(string):
    tmp_dict = dict()

    for _ in string.split():
        if _ not in tmp_dict:
            tmp_dict[_] = 1
        else:
            tmp_dict[_] = tmp_dict.get(_) + 1
    print(tmp_dict)


if __name__ == '__main__':
    string = "Gfg is best . Geeks are good and Geeks like Gfg"
    using_dict_comprehension(string)
    using_dict(string)
