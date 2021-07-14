def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)


def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n // 2))
    return b * exp_fast(b, n - 1)


def square(x):
    return x * x