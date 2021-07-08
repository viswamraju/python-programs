def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial_iter(n):
    if n == 0:
        return 1
    fact = 1
    while n >= 1:
        fact *= n
        n -= 1
    return fact


if __name__ == '__main__':
    n = 5
    print(factorial(n))
    print(factorial_iter(n))
