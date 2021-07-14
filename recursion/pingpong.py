def num_eights(x):
    if x <= 9:
        return 1 if x == 8 else 0
    if x % 10 == 8:
        return num_eights(x // 10) + 1
    return num_eights(x // 10)


ans = {1: 1, 2: 2}  # improves ET signnnnnnnnnnnnnificantly


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    """
    if n <= 0:
        return 0
    if n in ans:
        return ans[n]
    if n % 8 == 1 or num_eights(n - 1) >= 1:
        ans[n] = (
            pingpong(n - 1) - 1
            if pingpong(n - 1) - pingpong(n - 2) > 0
            else pingpong(n - 1) + 1
        )
    else:
        ans[n] = (
            pingpong(n - 1) + 1
            if pingpong(n - 1) - pingpong(n - 2) > 0
            else pingpong(n - 1) - 1
        )
    return ans[n]


def iterative_pingpong(n):
    value = 0
    dir = -1
    for i in range(1, n + 1):
        if i % 8 == 1 or num_eights(i - 1) >= 1:
            dir = -dir
        value += dir

    return value
