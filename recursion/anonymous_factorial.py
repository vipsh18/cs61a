from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: lambda k: f(f, k))(
        lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1)))
    )
