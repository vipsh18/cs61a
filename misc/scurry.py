def scurry(f, n):
    """Return a function that calls f on a list of arguments after being called n times.

    >>> scurry(sum, 4)(1)(1)(3)(2)
    7
    >>> scurry(len, 3)(7)([8])(-9)
    3
    """

    def h(k, args_so_far):
        if k == 0:
            return f(args_so_far)
        return lambda x: h(k - 1, args_so_far + [x])

    return h(n, [])