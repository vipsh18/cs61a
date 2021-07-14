def stable(s, k, n):
    """
    >>> stable([1, 2, 3, 5, 6], 1, 2)
    True
    >>> stable([1, 2, 3, 5, 6], 2, 2)
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2)
    False
    """
    for i in range(len(s)):
        near = range(max(0, i - k), i)
        if any([abs(s[i] - s[j]) > n for j in near]):
            return False
    return True