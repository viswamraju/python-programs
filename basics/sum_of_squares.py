def sum_of_n_squares(n):
    sum = 0
    for i in range(n+1):
        sum += i ** 2
    return sum


def sum_of_n_cubes(n):
    sum = 0
    for i in range(n+1):
        sum += i ** 3
    return sum


if __name__ == '__main__':
    print(sum_of_n_squares(5))
    print(sum_of_n_cubes(5))
