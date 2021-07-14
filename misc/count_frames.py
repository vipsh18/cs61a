def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 2) + fib(n - 1)


fib = count_frames(fib)
print(fib(20))
print(fib.open_count)
print(f"Maximum open frames: {fib.max_count}")