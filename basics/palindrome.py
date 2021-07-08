def is_palindrome(s):
    return s == s[::-1]


def is_palindrome_2(s):
    size = len(s)
    is_palind = False
    for i in range(int(size / 2) + 1):
        if s[i] != s[size - 1 - i]:
            break
    else:
        is_palind = True
    return is_palind


#  O(N3)  time complexity.   space complexity O(1)
def longest_palindrome_n3(s):
    max_length = 0
    max_sub_string = ""

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(max_sub_string) < len(word):
                    max_sub_string = word
                    max_length = len(word)
    return max_sub_string, max_length


def get_palindrome_substring(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1: r]


def longest_palindrome_n2(s):
    max_sub_str = ""

    for i in range(len(s)):
        odd = get_palindrome_substring(s, i, i)
        even = get_palindrome_substring(s, i, i+1)

        max_sub_str = max(max_sub_str, odd, even, key=len)

    return max_sub_str, len(max_sub_str)


print(longest_palindrome_n2("12maddam34"))



