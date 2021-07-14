def factorize(n, k=2):
    """Return the number of ways to factorize positive integer n. n should be expressed as product of non-decreasing integers >= k.

    >>> factorize(7) # 7
    1
    >>> factorize(12) # 2*2*3, 2*6, 3*4, 12
    4
    >>> factorize(12, 3) # 3*4, 12
    2
    >>> factorize(36) # 2*2*3*3, 2*2*9, 2*3*6, 2*18, 3*3*4, 3*12, 4*9, 6*6, 36
    9
    """
    if n == 1 or n == k:
        return 1
    elif k > n:
        return 0
    elif n % k != 0:
        return factorize(n, k + 1)
    return factorize(n, k + 1) + factorize(n // k, k)