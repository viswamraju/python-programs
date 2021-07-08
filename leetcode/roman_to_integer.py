def roman_to_integer(in_str):
    doubles = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    singles = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    size = len(s)
    i = 0
    integer = 0
    while i < size:
        if i < size - 1 and in_str[i:i+2] in doubles:
            integer += doubles[in_str[i:i+2]]
            i += 2
        else:
            integer += singles[in_str[i]]
            i += 1
    print(integer)


if __name__ == '__main__':
    s = "IVI"
    roman_to_integer(s)
