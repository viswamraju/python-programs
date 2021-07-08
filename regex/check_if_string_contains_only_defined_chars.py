import re


def check_string_contains_only_defined_chars(string, pattern):
    search = re.search(pattern, string)
    if search:
        print(search.group())
        print("Valid")
    else:
        print("Not valid")


pattern = re.compile('^[1234]+$')
check_string_contains_only_defined_chars("2153", pattern)
