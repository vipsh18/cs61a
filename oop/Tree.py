from oop.Link import square


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for branch in branches:
            assert isinstance(branch, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return f"Tree({repr(self.label)}{branch_str})"

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = "  " * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(
                    b,
                    indent + 1,
                )
            return tree_str

        return print_tree(self).rstrip()


def bst_min(t):
    if t.is_leaf():
        return t.label
    return min(
        t.label,
        bst_min(t.branches[0]),
    )


def bst_max(t):
    if t.is_leaf():
        return t.label
    return max(
        t.label,
        bst_max(t.branches[-1]),
    )


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    branches = t.branches
    if t.is_leaf():
        return True
    elif len(branches) == 1:
        return (
            is_bst(branches[0])
            and (t.label >= bst_min(branches[0]))
            or (t.label < bst_max(branches[0]))
        )
    elif len(branches) == 2:
        return (
            is_bst(branches[0])
            and is_bst(branches[1])
            and bst_max(branches[0]) <= t.label
            and bst_min(branches[1]) > t.label
        )
    else:
        return False


def bst_contains(b, item) -> bool:
    """Returns True if B contains ITEM.

    >>> b1 = Tree(2, [Tree(1), Tree(4, [Tree(3)])])
    >>> bst_contains(b1, 4)
    True
    >>> bst_contains(b1, 3)
    True
    >>> bst_contains(b1, 8)
    False
    >>> b2 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> bst_contains(b2, 2)
    True
    >>> bst_contains(b2, 5)
    False
    """
    if b.label == item:
        return True
    elif len(b.branches) == 1:
        return bst_contains(b.branches[0], item)
    elif len(b.branches) == 2:
        if b.label > item:
            return bst_contains(b.branches[0], item)
        return bst_contains(b.branches[1], item)
    return False


def in_order(b):
    """Returns the items in B, a binary search tree, in sorted
    order.

    >>> b1 = Tree(2, [Tree(1), Tree(4, [Tree(3)])])
    >>> in_order(b1)
    [1, 2, 3, 4]
    >>> singleton = Tree(4)
    >>> in_order(singleton)
    [4]
    """
    if b.is_leaf():
        return [b.label]
    if len(b.branches) == 1:
        return in_order(b.branches[0]) + [b.label]
    elif len(b.branches) == 2:
        return in_order(b.branches[0]) + [b.label] + in_order(b.branches[1])


def nth_largest(b, n):
    """Returns the Nth largest item in T.

    >>> b1 = Tree(2, [Tree(1), Tree(4, [Tree(3)])])
    >>> nth_largest(b1, 1)
    4
    >>> nth_largest(b1, 3)
    2
    >>> nth_largest(b1, 4)
    1
    """
    sorted_bst = in_order(b)
    return sorted_bst[-n] if sorted_bst[-n] else None


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def leaves(t):
    if t.is_leaf():
        return [t.label]
    all_leaves = []
    for b in t.branches:
        all_leaves.extend(leaves(b))
    return all_leaves


def height(t):
    if t.is_leaf():
        return 0
    return 1 + max([height(b) for b in t.branches])


def prune(t, n):
    """Prune all sub-trees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)


def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.
    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if t.label == value:
        yield [t.label]
    for b in t.branches:
        for path in path_yielder(b, value):
            yield [t.label] + path


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """

    def traverse(t):
        yield t.label
        for b in t.branches:
            yield from traverse(b)

    return list(traverse(t))


def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
        return t.label
    for b in t.branches:
        cumulative_mul(b)
        t.label *= b.label


def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    change = True

    def iterates_over_tree(t):
        nonlocal change
        branches = t.branches
        if len(branches) >= 2:
            for index in range(len(branches) // 2):
                iterates_over_tree(branches[index])
                if change == True:
                    (branches[index].label, branches[-index - 1].label,) = (
                        branches[-index - 1].label,
                        branches[index].label,
                    )
                change = not change

    iterates_over_tree(t)


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)


def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t.branches[0].label
    4
    >>> t.branches[0].branches[0].label
    9
    >>> t.branches[1].label
    16
    """
    t.label = square(t.label)
    for b in t.branches:
        square_tree(b)


def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        path = find_paths(b, entry)
        if path:
            path[0].insert(0, t.label)
            paths.extend(path)
    return paths


def combine_tree(t1, t2, combiner):
    """
    >>> from operator import mul
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    for (t1b, t2b) in zip(t1.branches, t2.branches):
        return Tree(combiner(t1.label, t2.label), [combine_tree(t1b, t2b, combiner)])


def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    change = True

    def map_element(t):
        nonlocal change
        if change:
            t.label = map_fn(t.label)
        change = not change
        if t.is_leaf():
            return Tree(t.label)
        for b in t.branches:
            map_element(b)
        return t

    return map_element(t)


def subtract_one(t):
    """Subtract one from every branch in the tree

    >>> t = Tree(5, [Tree(2, [Tree(8), Tree(1, [Tree(4)])]), Tree(3)])
    >>> subtract_one(t)
    Tree(4, [Tree(1, [Tree(7), Tree(0, [Tree(3)])]), Tree(2)])
    """
    return Tree(t.label - 1, [subtract_one(b) for b in t.branches])


def subtract_one_in_place(t):
    """Subtract one from every branch in the tree, in place

    >>> t = Tree(5, [Tree(2, [Tree(8), Tree(1, [Tree(4)])]), Tree(3)])
    >>> subtract_one_in_place(t)
    >>> t
    Tree(4, [Tree(1, [Tree(7), Tree(0, [Tree(3)])]), Tree(2)])
    """
    t.label -= 1
    for b in t.branches:
        subtract_one_in_place(b)


def equal(t1, t2) -> bool:
    """Returns Tree if t1 and t2 are equal trees.

    >>> t1 = Tree(1, [Tree(2, [Tree(4)]), Tree(3)])
    >>> t2 = Tree(1, [Tree(2, [Tree(4)]), Tree(3)])
    >>> equal(t1, t2)
    True
    >>> t3 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> equal(t1, t3)
    False
    """
    if t1.label != t2.label:
        return False
    elif len(t1.branches) != len(t2.branches):
        return False
    return all([equal(b1, b2) for b1, b2 in zip(t1.branches, t2.branches)])


def size(t):
    """Returns the number of elements in a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(4)]), Tree(3)])
    >>> size(t1)
    4
    """
    return 1 + sum([size(b) for b in t.branches])


def same_shape(t1, t2):
    """Takes two Trees and returns True if the trees have the same
    structure, but not necessarily the same entries.

    >>> t1 = Tree(1, [Tree(2, [Tree(4)]), Tree(3)])
    >>> t2 = Tree(1, [Tree(2, [Tree(4)]), Tree(3)])
    >>> same_shape(t1, t2)
    True
    >>> t3 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> same_shape(t1, t3)
    False
    """
    if t1.is_leaf() and t2.is_leaf():
        return True
    elif len(t1.branches) != len(t2.branches):
        return False
    return all([same_shape(b1, b2) for b1, b2 in zip(t1.branches, t2.branches)])


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t1
    Tree(1, [Tree(2), Tree(3)])
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> new1
    Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(4), Tree(5)])])
    >>> t2 = Tree(1, [Tree(2, [Tree(3)])])
    >>> t2
    Tree(1, [Tree(2, [Tree(3)])])
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> new2
    Tree(1, [Tree(2, [Tree(3, [Tree(6), Tree(1), Tree(2)])])])
    """
    if t.is_leaf():
        return Tree(t.label, [Tree(i) for i in vals])
    return Tree(t.label, [sprout_leaves(b, vals) for b in t.branches])


def prune_leaves(t, vals):
    """Takes a Tree and a list of values. For every leaf of the Tree, remove it if its entry is in the list of values.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> prune_leaves(t1, [1, 2, 3, 8])
    Tree(6, [Tree(2, [Tree(4)]), Tree(7, [Tree(7)])])
    """
    if t.is_leaf():
        if t.label not in vals:
            return t
        return None
    new_branches = [prune_leaves(b, vals) for b in t.branches]
    t.branches = [b for b in new_branches if b is not None]
    return t


def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    if len(t.branches) > n:
        sorted_labels = sorted([b.label for b in t.branches])[:n]
        for b in t.branches:
            prune_small(b, n)
            t.branches = [b for b in t.branches if b.label in sorted_labels]


"""Pluck leaves off a tree one by one.
Definitions:
1.  A "number tree" is a Tree whose labels are unique positive integers.
    No repeated labels appear in a number tree.

2.  A "plucking order" for a number tree t is a sequence of unique positive integers that are all labels of t.

3.  Valid plucking order if:
(a) plucking order contains all labels of t, and
(b) in the order, label for each node of t appears after labels of all its descendant nodes. Leaves appear first.
"""


def order(redwood) -> list:
    """Return a list containing a valid plucking order for labels of t.

    >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))              # only valid order
    [4, 3, 2, 1]
    >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]] # 2 valid orders
    True
    >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])])) # there are many valid orders
    >>> o.index(5) < o.index(4)                                      # but all have 5 before 4
    True
    >>> o.index(3) < o.index(2)                                      # and 3 before 2
    True
    >>> o[4:]                                                        # and 1 at the end
    [1]
    >>> order(Tree(7, [Tree(4, [Tree(6)]), Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], [6, 4, 5, 7]]
    True
    """
    plucking_order = []
    for b in redwood.branches:
        plucking_order += order(b)
    return plucking_order + [redwood.label]


def pluck(pine):
    """Return a function that returns whether a plucking order is valid
    for a number tree t when called repeatedly on elements of a plucking order.
    Calling the function shouldn't mutate pine.

    >>> b0 = Tree(2, [Tree(3, [Tree(4), Tree(5)])])
    >>> b1 = Tree(6, [Tree(7), Tree(8, [Tree(9)])])
    >>> t = Tree(1, [b0, b1])
    >>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)
    'success!'
    >>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)
    'success!'
    >>> pluck(t)(2)
    'Hey, not valid!'
    >>> pluck(b0)(5)(2)
    'Hey, not valid!'
    >>> pluck(b0)(4)(5)(3)(2)
    'success!'
    """

    def plucker(k):
        def pluck_one_leaf(cyprus):
            """Return a copy of cyprus w/o leaf k anf check that k is a
            leaf label, not an interior node label.
            """
            if cyprus.label == k:
                return "Hey, not valid!"
            plucked_branches = []
            for b in cyprus.branches:
                skip_this_leaf = b.is_leaf() and b.label == k
                if not skip_this_leaf:
                    plucked_branch_or_error = pluck_one_leaf(b)
                    if isinstance(plucked_branch_or_error, str):
                        return plucked_branch_or_error
                    else:
                        plucked_branches.append(plucked_branch_or_error)
            return Tree(cyprus.label, plucked_branches)

        nonlocal pine
        if pine.is_leaf():
            assert k == pine.label, "all k must appear in pine"
            return "success!"
        pine = pluck_one_leaf(pine)
        if isinstance(pine, str):
            return pine
        return plucker

    return plucker


def bigs(t) -> int:
    """Return the number of nodes in t that are larger than all their ancestors.

    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4
    """

    def f(a, x):
        if a.label > x:
            return 1 + sum([f(b, a.label) for b in a.branches])
        return sum([f(b, x) for b in a.branches])

    return f(t, t.label - 1)


def smalls(t) -> list:
    """Return the non-leaf nodes in t that are smaller than all their descendants.

    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """
    result = []

    def process(t):
        if t.is_leaf():
            return t.label
        smallest = min([process(b) for b in t.branches])
        if t.label < smallest:
            result.append(t)
        return min(smallest, t.label)

    process(t)
    return result


def long_paths(t, n):
    """Return a list of all paths in tree with length at least n.

    >>> whole = Tree(0, [Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(4), Tree(5)])]), Tree(13), Tree(6, [Tree(7, [Tree(8)]), Tree(9)]), Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    [0, 1, 2]
    [0, 1, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 3, 5]
    [0, 6, 7, 8]
    [0, 6, 9]
    [0, 11, 12, 13, 14]
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    [0, 1, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 3, 5]
    [0, 6, 7, 8]
    [0, 11, 12, 13, 14]
    >>> long_paths(whole, 4)
    [[0, 11, 12, 13, 14]]
    """
    paths = []

    def get_paths(te):
        own_paths = []
        if te.is_leaf():
            return [te.label]

        for b in te.branches:
            for path in get_paths(b):
                if isinstance(path, list):
                    own_paths.append([te.label] + path)
                else:
                    own_paths.append([te.label] + [path])

        for path in own_paths:
            paths.append(path)
        return own_paths

    get_paths(t)

    paths = list(filter(lambda x: len(x) > n and x[0] == t.label, paths))
    return paths