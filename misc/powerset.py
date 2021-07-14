def powerset(l):
    """
    >>> sorted(list(powerset([1, 2])))
    [[], [1], [1, 2], [2]]
    >>> sorted(list(powerset([1, 2, 3])))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    if len(l) <= 0:
        yield []
    else:
        for item in powerset(l[1:]):
            yield [l[0]] + item
            yield item