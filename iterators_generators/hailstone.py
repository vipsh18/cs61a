def hailstone(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n

    # Recursive implementation
    # if n <= 1:
    #     yield 1
    # else:
    #     yield n
    #     if n % 2 == 0:
    #         n //= 2
    #     else:
    #         n = 3 * n + 1
    #     yield from hailstone(n)


print(list(hailstone(51)))