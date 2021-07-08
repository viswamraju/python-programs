def stair_case_pattern(n):
    tmp_str = ""
    for i in range(0, n):
        k = i+1 if i % 2 != 0 else i
        spaces = (n-k) // 2
        tmp_str += "   " * spaces + " * " * k + "   " * spaces + "\n"
    print(tmp_str)


if __name__ == '__main__':
    stair_case_pattern(9)
