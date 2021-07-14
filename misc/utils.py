def min_abs_indices(s):
    """Indices of all elements in s that have least absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    # return [index for index, element in enumerate(s) if abs(element) == abs(min(s, key=abs))]
    min_abs = min(map(abs, s))
    return [i for i, e in enumerate(s) if abs(e) == min_abs]


def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    # return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    return max([x + y for x, y in zip(s[:-1], s[1:])])


def digit_dict(s):
    """Map each digit d to the the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    last_digits = [x % 10 for x in s]
    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits}


def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return all([s[i] in s[:i] + s[i + 1 :] for i in range(len(s) - 1)])
