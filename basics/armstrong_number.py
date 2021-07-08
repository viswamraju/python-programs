def is_arm_strong_number(tmp):
    num = tmp
    exp = len(str(num))
    print(exp)
    s = 0
    while num > 0:
        digit = num % 10
        s += digit ** exp
        num = num // 10

    return tmp == s


if __name__ == '__main__':
    n = 153
    print(is_arm_strong_number(n))

