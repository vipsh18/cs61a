def amon(g):
    n = 0

    def u(s):
        nonlocal n
        f = lambda x: x + g.pop() + n
        n += 1
        return f(s)

    return u


g = [1, 2, 3]
skeld = amon(g)
pink = skeld(1)
purple = skeld(2)