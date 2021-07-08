def longest_substring_no_dups(string):
    used = {}
    start = 0
    max_length = 0
    max_str = ""
    for i, v in enumerate(string):
        if v in used and start <= used[v]:
            start = used[v] + 1
        else:
            max_length = max(max_length, i - start + 1)
            max_str = string[start: start + max_length]
        used[v] = i
    print(max_length)
    print(max_str)


if __name__ == '__main__':
    # string = "abcabcdbb"
    string = "pwwkew"
    longest_substring_no_dups(string)
