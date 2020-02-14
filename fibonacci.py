
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache1 = 0
    cache2 = 1

    for i in range(2, n + 1):
        z = cache1 + cache2
        cache1 = cache2
        cache2 = z

    return cache2

cache = { 0 : 0, 1: 1 }
def fibonacci_usingMemoization(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        return 0
    if n in cache:
        return cache[n]
    x = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = x
    return x


for i in range(5, 100):
    print("fib of {} is {}".format(i, fibonacci(i)))