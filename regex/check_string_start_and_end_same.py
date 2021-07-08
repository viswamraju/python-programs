import re


def check_start_end_same(in_str):
    pattern = re.compile(r"^[a-z]$|^([a-z]).*\1$")
    search = re.search(pattern, in_str)
    if search:
        print(search.group())
    else:
        print("No match")

if __name__ == '__main__':
    in_str = "bcdb"
    check_start_end_same(in_str)