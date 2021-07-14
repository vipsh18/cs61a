def close(n, smallest=10, d=10):
    """

    >>> close(123)
    123
    >>> close(153)
    153
    >>> close(15123)
    1123
    >>> close(111111111)
    11
    >>> close(985357)
    557
    >>> close(14735476)
    143576
    >>> close(812348567)
    1234567
    >>> close(45671)
    4567
    """
    if n == 0:
        return 0
    no = close(n // 10, smallest, d)
    if smallest > n % 10:
        yes = close(n // 10, min(smallest, d), n % 10) * 10 + n % 10
        return max(no, yes)
    return no