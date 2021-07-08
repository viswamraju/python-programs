#
# Using Generator
#
# def fib_n(n):
#     fib = [0, 1]
#     i = 2
#     yield 0
#     yield 1
#     while i < n:
#         val = fib[i-2] + fib[i-1]
#         yield val
#         fib.append(val)
#         i += 1
#
#
# for _ in fib_n(10):
#     print(_)

# --------------------------------------------------

# Using recursion

# def fib_n(n):
#     if n < 2:
#         return n
#     else:
#         return fib_n(n-2) + fib_n(n-1)

def fibonosci(n, k):
    # nth multiple of k
    fib = [0, 1]
    i = 2
    multiples_count = 0
    while True:
        val = fib[i-1] + fib[i-2]
        fib.append(val)
        i += 1
        if val % k == 0:
            multiples_count += 1
        if multiples_count == n:
            break
    return i-1, fib[i-1]


print(fibonosci(5, 5))
