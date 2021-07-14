def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 2) + fib(n - 1)


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


fib = memo(fib)
print(fib(30))
print(fib(50))
print(fib(300))
