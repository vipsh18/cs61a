def recursive_merge(m, n):
    def maintain_digits(m, n, digits):
        if m == 0 and n // 10 == 0:
            return (n % 10) * (10 ** digits)
        if n == 0 and m // 10 == 0:
            return (m % 10) * (10 ** digits)
        if m % 10 < n % 10 or n == 0 or m % 10 == n % 10:
            return (m % 10) * (10 ** digits) + maintain_digits(m // 10, n, digits + 1)
        if n % 10 < m % 10 or m == 0:
            return (n % 10) * (10 ** digits) + maintain_digits(m, n // 10, digits + 1)

    return maintain_digits(m, n, 0)


print(recursive_merge(31, 42))
print(recursive_merge(21, 0))
print(recursive_merge(21, 31))
