import re


def upper_case_followed_by_lowercase_letters(in_str):
    pattern = re.compile("^[A-Z]+[a-z]+$")


if __name__ == '__main__':
    in_str = "Geeks"
    upper_case_followed_by_lowercase_letters(in_str)
