res = {}

def count_stair_ways(n, k):
    # just the base cases
	if k > n:
		k = n
	if n == 0 or k == 1:
		return 1
	if n < 0 or k == 0:
		return 0

	# stops recursing lots of times
	if n in res:
		if k in res[n]:
			return res[n][k]

	total = 0
	for i in range(1, k + 1):
		total += count_stair_ways(n - i, k)
		if n not in res:
			res[n] = {}
		res[n][k] = total
	return total

print(count_stair_ways(10, 3))