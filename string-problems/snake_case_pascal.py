import string


def using_title(in_str):
    print(in_str.replace("_", " ").title().replace(" ", ""))


def using_capwords(in_str):
    print(string.capwords(in_str, "_").replace("_", ""))


if __name__ == '__main__':
    in_str = "geeksforgeeks_is_best"
    # susing_title(in_str)
    using_capwords(in_str)