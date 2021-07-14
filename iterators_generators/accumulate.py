from operator import add, mul


def accumulate(iterable, f):
    """Takes in an iterable and a function f and yields each accumulated value from applying f to the running total and the next element.
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    curr = 1 if f == mul else 0
    for num in it:
        curr = f(num, curr)
        yield curr