def add_chars(w1, w2):
    """
    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """

    if len(w1) == 0:
        return w2

    # implementation 1:
    if w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    else:
        return w2[0] + add_chars(w1, w2[1:])

    # implementation 2:
    # if w1 == w2:
    #     return ''
    # if w2[0] not in w1:
    #     return w2[0] + add_chars(w1, w2[1:])
    # else:
    #     return add_chars(w1.replace(w2[0], '', 1), w2[1:])


chars = add_chars("coy", "cacophony")
print(f"Characters to be added: {chars if len(chars) > 0 else None}")
