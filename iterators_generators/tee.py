def tee(iterable):
    it = iter(iterable)
    queues = [[], []]

    def gen(lst):
        while True:
            if not lst:
                try:
                    value = next(it)
                except StopIteration:
                    return
                for q in queues:
                    q.append(value)
            yield lst.pop(0)

    return [gen(queues[0]), gen(queues[1])]


yum = ["avocado", "quinoa", "cream cheese"]
