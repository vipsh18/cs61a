from functools import wraps


# decorator to trace execution of recursive function
def trace(func):

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = "|  "

    # current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        print(
            f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})'
        )
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        print(f"{separator * (trace.recursion_depth + 1)}|-- return {result}")

        return result

    return traced_func


def next_largest_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    """

    # @trace
    def constrained_count(total, smallest_coin):
        if total == 0:
            return 1
        if total < 0 or smallest_coin == None:
            return 0
        return constrained_count(
            total, next_largest_coin(smallest_coin)
        ) + constrained_count(total - smallest_coin, smallest_coin)

    return constrained_count(total, 1)


print(count_coins(15))