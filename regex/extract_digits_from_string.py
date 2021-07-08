import re


def extract_digits_from_string(string):
    print(string)
    pattern = re.compile(r"\d+")
    matches = re.findall(pattern, string)
    if matches:
        print(matches)
    else:
        print("No matches")


if __name__ == '__main__':
    string = "abc1234m 6, 8, 9 10 hig"
    extract_digits_from_string(string)