from operator import add, mul, sub


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return f"Link({repr(self.first)}{rest_repr})"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        self = self.rest
        return self.__getitem__(i - 1)

    def get(self, i):
        return self.__getitem__(i)


def square(x):
    return x * x


def odd(x):
    return x % 2 == 1


def range_link(start, end) -> Link:
    """
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))


def map_link(f, s) -> Link:
    """
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s) -> Link:
    """
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    return filtered_rest


def non_mutating_add(s, v) -> Link:
    """
    Non-mutating add
    >>> s = Link(1, Link(3, Link(5)))
    >>> non_mutating_add(s, 4)
    Link(1, Link(3, Link(4, Link(5))))
    >>> non_mutating_add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> non_mutating_add(s, 6)
    Link(1, Link(3, Link(5, Link(6))))
    >>> non_mutating_add(s, 3)
    Link(1, Link(3, Link(5)))
    """
    if s is Link.empty:
        return Link(v, Link.empty)
    if s.first == v:
        return s
    elif s.first > v:
        return Link(v, s)
    return Link(s.first, non_mutating_add(s.rest, v))


def add(s, v) -> Link:
    """
    Mutating add
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


def store_digits(n) -> Link:
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    n, last = n // 10, n % 10
    prev = Link(last)

    def save_links(n, prev):
        if n <= 0:
            return prev
        n, last = n // 10, n % 10
        prev = Link(last, prev)
        return save_links(n, prev)

    return save_links(n, prev)


def extend_link(s, t):
    if s is Link.empty:
        return t
    return Link(s.first, extend_link(s.rest, t))


Link.__add__ = extend_link


def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    return str(s.first) + separator + join_link(s.rest, separator)


def link_iterator(link):
    if link is not Link.empty:
        yield link.first
        yield from link_iterator(link.rest)


def convert_link(link) -> list:
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    #########################################
    # iterative
    #########################################
    # elements = []
    # while link is not Link.empty:
    #     elements.append(link.first)
    #     link = link.rest
    # return elements
    #########################################
    # recursive
    #########################################
    if link is Link.empty:
        return []
    return [link.first] + convert_link(link.rest)


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if s is Link.empty or s.rest is Link.empty:
        return
    s.rest = s.rest.rest
    every_other(s.rest)


def has_cycle(link) -> bool:
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    seen = []
    while link is not Link.empty:
        if link in seen:
            return True
        seen.append(link)
        link = link.rest
    return False


def has_cycle_constant(link) -> bool:
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    if link is Link.empty:
        return False
    slow, fast = link, link.rest
    while fast is not Link.empty:
        if fast.rest is Link.empty:
            return False
        elif fast is slow or fast.rest is slow:
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest
    return False


def sum_nums(link) -> int:
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if link is Link.empty:
        return 0
    return link.first + sum_nums(link.rest)


import math


def multiply_links(lst_of_links) -> Link:
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_links([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    if any([link is Link.empty for link in lst_of_links]):
        return Link.empty
    first = math.prod([link.first for link in lst_of_links])
    rest_links = [link.rest for link in lst_of_links]
    return Link(first, multiply_links(rest_links))


def flip_two(lnk) -> Link:
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    while lnk.rest is not Link.empty:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        lnk = lnk.rest.rest


def shuffle(lnk):
    """
    >>> shuffle(Link(1, Link(2, Link(3, Link(4)))))
    Link(2, Link(1, Link(4, Link(3))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    new_head = lnk.rest
    lnk.rest = shuffle(new_head.rest)
    new_head.rest = lnk
    return new_head


def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        first = link.first
        if f(first) == True:
            yield first
        link = link.rest


def filter_link_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link_no_iter(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    first = link.first
    if f(first) == True:
        yield first
    yield from filter_link_no_iter(link.rest, f)


def ordered(link, key=lambda x: x) -> bool:
    """Returns whether a Linked List is ordered from least to greatest

    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(1, Link(4, Link(3))), key=abs)
    False
    """
    if link is Link.empty or link.rest is Link.empty:
        return True
    if key(link.first) > key(link.rest.first):
        return False
    return ordered(link.rest)


def merge(s, t) -> Link:
    """Create a sorted link containing all elements of both sorted Links s & t

    >>> s = Link(1, Link(5))
    >>> t = Link(1, Link(4))
    >>> merge(s, t)
    Link(1, Link(1, Link(4, Link(5))))
    >>> s
    Link(1, Link(5))
    >>> t
    Link(1, Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    return Link(t.first, merge(s, t.rest))


def merge_in_place(s, t) -> Link:
    """Create a sorted link containing all elements of both sorted Link s & t

    >>> s = Link(1, Link(5))
    >>> t = Link(1, Link(4))
    >>> merge_in_place(s, t)
    Link(1, Link(1, Link(4, Link(5))))
    >>> s
    Link(1, Link(1, Link(4, Link(5))))
    >>> t
    Link(1, Link(4, Link(5)))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    t.rest = merge_in_place(s, t.rest)
    return t


def trim(s, index):
    """Mutate s so that all elements that occur after index are removed.
    Return a Linked List of all removed elements. If index exceeds
    Linked List, raise IndexError.

    >>> s1 = Link(1, Link(2, Link(3)))
    >>> trim(s1, 0)
    Link(2, Link(3))
    >>> s1
    Link(1)
    >>> s2 = Link(1, Link(2, Link(3)))
    >>> trim(s2, 2)
    >>> s2
    Link(1, Link(2, Link(3)))
    >>> s3 = Link(1, Link(2, Link(3)))
    >>> trim(s3, 3)
    Traceback (most recent call last):
        ...
    IndexError
    """
    if s is Link.empty:
        raise IndexError
    elif index == 0:
        temp = s.rest
        s.rest = Link.empty
        return temp if temp != Link.empty else None
    else:
        return trim(s.rest, index - 1)


def extend_link_in_place(s, t) -> None:
    """
    >>> s1 = Link(1)
    >>> s2 = Link(2, Link(3))
    >>> extend_link_in_place(s1, s2)
    >>> s1
    Link(1, Link(2, Link(3)))
    >>> s1.rest is not s2
    True
    """
    if t is not Link.empty:
        s.rest = Link(t.first)
        extend_link_in_place(s.rest, t.rest)


def deep_map(fn, lnk):
    """Applies fn to every element in lnk.

    >>> normal = Link(1, Link(2, Link(3)))
    >>> deep_map(lambda x: x * x, normal)
    >>> normal
    Link(1, Link(4, Link(9)))
    >>> nested = Link(Link(1, Link(2)), Link(3, Link(4)))
    >>> deep_map(lambda x: x * x, nested)
    >>> nested
    Link(Link(1, Link(4)), Link(9, Link(16)))
    """
    if lnk is Link.empty:
        return
    if type(lnk.first) == Link:
        deep_map(fn, lnk.first)
    else:
        lnk.first = fn(lnk.first)
    deep_map(fn, lnk.rest)


def list_to_link(lst):
    """Converts a list to Linked List

    >>> list_to_link([1, 2, 3, 4])
    Link(1, Link(2, Link(3, Link(4))))
    """
    if len(lst) == 1:
        return Link(lst[0])
    return Link(lst[0], list_to_link(lst[1:]))


def reverse_link(lnk):
    """Reverse a linked list. Create a new link.

    >>> lnk2 = Link(1, Link(2, Link(3)))
    >>> reverse_link(lnk2)
    Link(3, Link(2, Link(1)))
    """
    reversed_list = list(reversed(convert_link(lnk)))
    return list_to_link(reversed_list)


def count(r, value):
    """Counts the number of times VALUE shows up in r.

    >>> r = Link(3, Link(3, Link(2, Link(3))))
    >>> count(r, 3)
    3
    >>> count(r, 2)
    1
    """
    #########################################
    # iterative
    #########################################
    # num = 0
    # while r is not Link.empty:
    #     if r.first == value:
    #         num += 1
    #     r = r.rest
    # return num
    #########################################
    # recursive
    #########################################
    if r is Link.empty:
        return 0
    if r.first == value:
        return 1 + count(r.rest, value)
    return count(r.rest, value)


def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list.

    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
    if lnk is Link.empty:
        return 0
    elif not isinstance(lnk.first, Link):
        return 1 + deep_len(lnk.rest)
    else:
        return deep_len(lnk.first) + deep_len(lnk.rest)


def make_to_string(front, mid, back, empty_repr):
    """Returns a function that turns linked lists to strings.

    >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kevins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kevins_to_string(Link.empty)
    '[]'
    >>> jerrys_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> jerrys_to_string(Link.empty)
    '()'
    """

    def printer(lnk):
        if lnk is Link.empty:
            return empty_repr
        return f"{front}{lnk.first}{mid}{printer(lnk.rest)}{back}"

    return printer


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    Traceback (most recent call last):
        ...
    IndexError
    """
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link.rest is Link.empty:
        raise IndexError
    else:
        insert(link.rest, value, index - 1)


def foldl(link, fn, z):
    """Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    return foldl(link.rest, fn, fn(z, link.first))


def remove_duplicates(lnk):
    """Takes a sorted linked list of integers and mutates it so that all duplicates are removed.
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    seen = [lnk.first]
    temp, prev = lnk.rest, lnk
    while temp is not Link.empty:
        if temp.first in seen:
            prev.rest = temp.rest
        else:
            seen.append(temp.first)
            prev = temp
        temp = temp.rest


def filterl(lst, pred):
    """Filters LST based on PRED
    >>> lst = Link(4, Link(3, Link(2, Link(1))))
    >>> filterl(lst, lambda x: x % 2 == 0)
    Link(4, Link(2))
    >>> lst2 = Link(3, Link(4, Link(1, Link(2))))
    >>> filterl(lst2, lambda x: x % 2 == 0)
    Link(4, Link(2))
    """
    temp, prev = lst, lst
    while prev == temp:
        if not pred(temp.first):
            lst = lst.rest
            prev = temp
        temp = temp.rest
    while temp is not Link.empty:
        if not pred(temp.first):
            prev.rest = temp.rest
        else:
            prev = temp
        temp = temp.rest
    return lst