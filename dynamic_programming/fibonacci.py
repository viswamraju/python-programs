
"""
Time consuming
Time complexity  O(2^n)

                7
        6               5
    5       4       4       3
  4   3   3   2   3   2    2   1
  .......

Space Complexity
    Always we will have not more than N in method stack
    So space complexity is O(n)
"""


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
"""
dynamic programming

"""


def fibd(n, mem={}):
    if n <= 2:
        return 1
    if n in mem:
        return mem[n]

    mem[n] = fibd(n-1, mem) + fibd(n-2, mem)
    return mem[n]


if __name__ == '__main__':
    print(fibd(5))
    print(fibd(6))
    print(fibd(7))
    print(fibd(50))
