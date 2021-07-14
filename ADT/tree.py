def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])


def count_leaves(t):
    if is_leaf(t):
        return 1
    return sum([count_leaves(b) for b in branches(t)])


def leaves(t):
    if is_leaf(t):
        return [label(t)]
    return sum([leaves(i) for i in branches(t)], [])


def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    bs = [increment_leaves(b) for b in branches(t)]
    return tree(label(t), bs)


def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


def print_tree(t, indent=0):
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def print_sums(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    if label(t) == "berry":
        return True
    for b in branches(t):
        if berry_finder(b):
            return True
    return False


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    # if not t1:
    #     return t2
    # if not t2:
    #     return t1
    # new_label = label(t1) + label(t2)
    # t1_children, t2_children = branches(t1), branches(t2)
    # length_t1, length_t2 = len(t1_children), len(t2_children)
    # if length_t1 < length_t2:
    #     t1_children += [None for _ in range(length_t1, length_t2)]
    # elif len(t1_children) > len(t2_children):
    #     t2_children += [None for _ in range(length_t2, length_t1)]
    # return tree(
    #     new_label,
    #     [add_trees(child1, child2) for child1, child2 in zip(t1_children, t2_children)],
    # )

    # implementation 2
    # result_label = label(t1) + label(t2)
    # result_branches = []
    # i = 0
    # while i < len(branches(t1)) and i < len(branches(t2)):
    #     b1, b2 = branches(t1)[i], branches(t2)[i]
    #     new_branch = add_trees(b1, b2)
    #     result_branches += [new_branch]
    #     i += 1
    # result_branches += branches(t1)[i:]
    # result_branches += branches(t2)[i:]
    # return tree(result_label, result_branches)

    # implementation 3
    result_label = label(t1) + label(t2)
    result_branches = [add_trees(b1, b2) for b1, b2 in zip(branches(t1), branches(t2))]
    i = len(result_branches)
    result_branches += branches(t1)[i:]
    result_branches += branches(t2)[i:]
    return tree(result_label, result_branches)


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t), [tree(leaf) for leaf in leaves])
    return tree(label(t), [sprout_leaves(s, leaves) for s in branches(t)])


def height(t):
    """
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])


def max_path_sum(t):
    """
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    >>> t2 = tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)])
    >>> max_path_sum(t2)
    10
    """
    if is_leaf(t):
        return label(t)
    return label(t) + max([max_path_sum(b) for b in branches(t)])


def square_tree(t):
    """
    >>> numbers = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    sq_branches = [square_tree(b) for b in branches(t)]
    return tree(label(t) ** 2, sq_branches)


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    """
    if label(tree) == x:
        return [x]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path


def subtract_one(t):
    return tree(label(t) - 1, [subtract_one(b) for b in branches(t)])


def contains(t, e) -> bool:
    """Implement a function contains, which takes a tree t and an
    element e. contains will return True if t contains the
    element e, and False otherwise.

    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> contains(t, 6)
    True
    >>> contains(t, 4)
    False
    """
    if label(t) == e:
        return True
    return any([contains(b, e) for b in branches(t)])


def all_paths(t):
    """Implement a function all_paths, which takes a tree t.
    all_paths will return a list of paths from the root to
    each leaf.

    >>> t = tree(5, [tree(3, [tree(2), tree(1)]), tree(6)])
    >>> all_paths(t)
    [[5, 3, 2], [5, 3, 1], [5, 6]]
    """
    if is_leaf(t):
        return [t]
    return [[label(t)] + path for b in branches(t) for path in all_paths(b)]


def max_tree(t):
    """Implement a function max_tree, which takes a tree t. It returns a
    new tree with the exact same structure as t; at each node in the new
    tree, the entry is the largest number that is contained in that
    node's subtrees or the corresponding node in t

    >>> t = tree(5, [tree(3, [tree(2), tree(4)]), tree(6)])
    >>> print_tree(max_tree(t))
    6
      4
        2
        4
      6
    """
    if is_leaf(t):
        return tree(label(t))
    new_branches = [max_tree(b) for b in branches(t)]
    new_label = max([label(t)] + [label(b) for b in new_branches])
    return tree(new_label, new_branches)


# t = tree(7, [tree(1, [tree(3, [tree(2, [tree(-4), tree(0)]), tree(8, [tree(6)])]), tree(11, [tree(16, [tree(17)])])]), tree(19, [tree(20)])])

t2 = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
