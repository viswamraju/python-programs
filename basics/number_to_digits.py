def num_to_digits(num):
    digits = []

    while num > 0:
        digit = num % 10
        digits.insert(0, digit)
        num = num // 10

    return digits


if __name__ == '__main__':
    n = 987
    print(num_to_digits(n))
