def reverse(g):
    """
    Generates the value of a finite generator g in reverse order
    >>> def first_n_naturals(n):
    ...     for i in range(n):
    ...         yield i
    >>> reverse_naturals = reverse(first_n_naturals(5))
    >>> list(reverse_naturals)
    [4, 3, 2, 1, 0]
    """
    try:
        value = next(g)
        yield from reverse(g)
        yield value
    except StopIteration:
        pass
