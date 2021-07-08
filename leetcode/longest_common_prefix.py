def longest_common_prefix(lst):
    i = 0
    common_prefix = ""
    for _ in zip(*lst):
        if all([_.count(_[0]) == len(_)]):
            common_prefix += _[0]
    print(common_prefix)


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    longest_common_prefix(strs)



