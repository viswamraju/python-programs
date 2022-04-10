"""
Calculate how many ways we can reach from start to end.
We can move either right or down

Given 3 * 3 matrix

ways to reach from start to end = ways(2 * 3) + ways (3 * 2)
"""
import time


def grid_traveller(m, n):
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1

    return grid_traveller(m-1, n) + grid_traveller(m, n-1)


def grid_traveller_dyn(m, n, memo={}):
    if (m, n) in memo or (n, m) in memo: return memo[(m, n)]
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    memo[(m, n)] = grid_traveller_dyn(m-1, n, memo) + grid_traveller_dyn(m, n-1, memo)
    memo[(n, m)] = memo[(m, n)]
    return memo[(m, n)]


if __name__ == '__main__':
    start = time.time_ns()
    print(grid_traveller_dyn(2, 3))
    print(grid_traveller_dyn(3, 2))
    print(grid_traveller_dyn(3, 3))
    print(grid_traveller_dyn(100, 100))
    print(time.time_ns() - start)


