import re


def is_exists_sub_str(string, sub_str):
    if sub_str in string:
        print("YES")
    else:
        print("NO")


def is_exists_sub_str_find(string, sub_str):
    if string.find(sub_str) != -1:
        print("YES")
    else:
        print("NO")


def is_exists_sub_str_count(string, sub_str):
    if string.count(sub_str) > 0:
        print("YES")
    else:
        print("NO")


def is_exists_sub_str_re(string, sub_str):
    if re.search(sub_str, string):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    is_exists_sub_str_re("geeks for geeks", "geek")
