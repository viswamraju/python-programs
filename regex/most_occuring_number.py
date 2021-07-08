import re


def most_occured_number(in_str):
    pattern = re.compile("[0-9]+")
    nums = re.findall(pattern, in_str)
    num_dict = dict()

    for _ in nums:
        if _ in num_dict:
            num_dict[_] = num_dict[_] + 1
        else:
            num_dict[_] = 1

    print(num_dict)
    max_occured_key = ""
    max_occurences = 0
    for key, value in num_dict.items():
        if value > max_occurences:
            max_occurences = value
            max_occured_key = key
    print(max_occured_key)


if __name__ == '__main__':
    in_str1 = "geek55of55geeks4abc3dr2"
    in_str2 = "abcd1def2high2bnasvd3vjhd44"
    most_occured_number(in_str2)