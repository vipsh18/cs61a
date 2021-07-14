def max_product(s):
    """
    Return the maximum product that can be formed using non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) <= 2:
        return max(s) if len(s) >= 1 else 1
    if len(s) == 3:
        return max(s[0] * s[2], s[1])
    return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))


print(max_product([10, 3, 9, 1, 5]))