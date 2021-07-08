def get_common_factors(x, y):
    x_factors = [i for i in range(1, x+1) if x % i == 0]
    y_factors = [i for i in range(1, y+1) if y % i == 0]

    print(x_factors, y_factors)
    print(set(x_factors).intersection(set(y_factors)))


def get_common_factors_2(x, y):
    common_factors = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            common_factors.append(i)
    print(common_factors)

if __name__ == '__main__':
    x = 10
    y = 15
    # get_common_factors(x, y)
    get_common_factors_2(x, y)
