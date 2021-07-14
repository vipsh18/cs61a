class Adele:
    times = "1000"

    def __init__(self, you):
        self.call = you

    def __str__(self):
        return self.times


class Hello(Adele):
    def __next__(self):
        return next(self.call)


never = iter("scheme2Bhome")


def any(more):
    next(never)
    print(outside)
    yield next(never)
    print(next(never))
    yield more(more)


outside = Hello(any(any))
print(next(never))
print(next(outside))
print(next(next(outside)))
print(list(never)[:3])
print(next(next(outside)))