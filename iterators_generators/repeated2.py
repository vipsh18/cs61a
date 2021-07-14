def repeated(f):
    """Yields functions that are repeated applications of a one-argument function f. The first function yielded should apply f 0 times (the identity function), the second function yielded should apply f once, etc.

    >>> double = lambda x: x * 2
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> identity(1)
    1
    >>> double(1)
    2
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        yield g
        g = (lambda g: lambda x: f(g(x)))(g)