def reverse_integer(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = num * -1

    order = len(str(num)) - 1
    revered_num = 0
    while num > 0:
        digit = num % 10
        revered_num += digit * (10 ** order)
        num = num // 10
        order -= 1
    if is_negative:
        revered_num = -1 * revered_num
    print(revered_num)


if __name__ == '__main__':
    num = -123
    reverse_integer(num)
