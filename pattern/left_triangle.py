def left_triangle(n):
    tmp_str = ""
    for i in range(1, n+1):
        tmp_str += "* " * i + " " * (n+1-i) + "\n"

    print(tmp_str)


def right_triangle(n):
    tmp_str = ""
    for i in range(1, n+1):
        tmp_str += "   " * (n + 1 - i) + " * " * i + "\n"

    print(tmp_str)


if __name__ == '__main__':
    n = 5
    # left_triangle(n)
    right_triangle(n)
