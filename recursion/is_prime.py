def is_prime(n):
    if n == 1:
        return False

    def prime_helper(num, still_prime):
        if num == 1:
            return still_prime
        if n % num == 0:
            still_prime = False
        else:
            return prime_helper(num - 1, still_prime)
        return still_prime

    return prime_helper(n - 1, True)


print(is_prime(7))
print(is_prime(8))
print(is_prime(10))
print(is_prime(0))