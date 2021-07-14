def count_stair_ways(n):
    if n in [0, 1, 2, 3]:
        return n
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


print(count_stair_ways(4))