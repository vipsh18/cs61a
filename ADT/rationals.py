from math import gcd


def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def equal_rational(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rational(x):
    print(f"{numer(x)} / {denom(x)}")
    return None


def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]