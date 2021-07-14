def max_subseq(n, t):
    """Return the maximum subsequence of length at most t that can be found in the given number n
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    if t == 0:
        return 0
    if n <= 9:
        return n
    last_digit = n % 10
    rest = n // 10

    keep_last_digit = max_subseq(rest, t - 1) * 10 + last_digit
    drop_last_digit = max_subseq(rest, t)
    return max(keep_last_digit, drop_last_digit)