def amplify(f, x):
    """
    Yield the longest sequence x, f(x), f(f(x)), ... that are all true values
    >>> list(amplify(lambda x: x[1:], "boxes"))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2 - 1, 14))
    [14, 6, 2]
    """
    while x:
        yield x
        x = f(x)