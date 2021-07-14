def make_sassy_function(f, msg):
    """Returns a version of f that only works every other function
    call.

    >>> f = lambda x: x**2
    >>> sassy_f = make_sassy_function(f, 'Um, excuse me?')
    >>> sassy_f(4)
    16
    >>> sassy_f(5)
    'Um, excuse me?'
    >>> sassy_f(6)
    36
    >>> g = lambda x, y: x*y
    >>> sassy_g = make_sassy_function(g, "Ain't nobody got time for that!")
    >>> sassy_g(1, 2)
    2
    >>> sassy_g(5, 4)
    "Ain't nobody got time for that!"
    """
    sassy = True

    def put_the_sass_in(*args):
        nonlocal sassy
        sassy = not sassy
        if sassy:
            return msg
        return f(*args)

    return put_the_sass_in