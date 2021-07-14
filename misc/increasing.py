def increasing(n, smallest=10):
    """Return the largest sequence of digits within n that is increasing.

    >>> increasing(87247861)
    2478
    >>> increasing(367456751)
    34567
    """
    if n == 0:
        return 0
    no = increasing(n // 10, smallest)
    if n % 10 < smallest:
        yes = increasing(n // 10, min(n % 10, smallest)) * 10 + n % 10
        return max(no, yes)
    return no