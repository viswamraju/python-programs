def prime_numbers_between_range(start, end):
    for num in range(100, 200):
        if all([(num % i) != 0 for i in range(2, num//2)]):
            print(num)


if __name__ == '__main__':
    start = 100
    end = 200
    prime_numbers_between_range(start, end)
    print(9 % 2)
