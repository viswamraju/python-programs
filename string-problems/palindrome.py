def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def longest_palindrome_in_str_1(string):
    size = len(string)
    max_sub_str = string[0]
    for i in range(size):
        tmp_str = string[i]
        for j in range(i+1, size):
            tmp_str += string[j]
            if is_palindrome(tmp_str):
                max_sub_str = max(max_sub_str, tmp_str, key=len)
    print(max_sub_str)


def check_max_palindrome(string, l, r):
    size = len(string)
    while l >= 0 and r < size and string[l] == string[r]:
        l -= 1
        r += 1
    return string[l+1: r]


def longest_palindrome_in_str_2(string):
    res = ""
    size = len(string)
    for i in range(size):
        odd = check_max_palindrome(string, i, i)
        even = check_max_palindrome(string, i, i+1)
        res = max(res, odd, even, key=len)
    print(res)


if __name__ == '__main__':
    string = "madam1"
    # print(is_palindrome(string))
    longest_palindrome_in_str_2(string)
