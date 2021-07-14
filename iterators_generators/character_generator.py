def char_gen(s):
    """
    >>> for char in char_gen("hello"):
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    """
    for i in s:
        yield i