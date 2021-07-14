def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    """
    if n <= 9:
        return 0
    elif n <= 99:
        return max(n % 10 - (n // 10) - 1, 0)
    return missing_digits(n // 10) + missing_digits(n % 100)


# Alternate implementation using strings!
# def missing_digits(n):
#     str_n = str(n)
#     if n // 10 == 0 or n % 10 - int(str_n[0]) <= 1:
#         return 0
#     if n // 10 <= 9:
#         return len([i for i in range(int(str_n[0]) + 1, n % 10)])
#     return missing_digits(int(str_n[: len(str_n) // 2 + 1])) + missing_digits(
#         int(str_n[len(str_n) // 2 :])
#     )
