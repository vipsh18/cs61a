def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    goal = [m - 1, n - 1]

    def calc_paths(m, n):
        start = [m, n]
        if start == goal:
            return 1
        elif start[0] != goal[0] and start[1] != goal[1]:
            return calc_paths(start[0] + 1, start[1]) + calc_paths(
                start[0], start[1] + 1
            )
        elif start[0] != goal[0]:
            return calc_paths(start[0] + 1, start[1])
        elif start[1] != goal[1]:
            return calc_paths(start[0], start[1] + 1)

    return calc_paths(0, 0)