def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_counter = 0

    def global_counter_maker():
        local_counter = 0

        def local_counter_maker(task):
            nonlocal local_counter, global_counter
            if task == "count":
                local_counter += 1
                return local_counter
            elif task == "global-count":
                global_counter += 1
                return global_counter
            elif task == "reset":
                local_counter = 0
            else:
                global_counter = 0

        return local_counter_maker

    return global_counter_maker