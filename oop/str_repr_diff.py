class Bear:
    """A Bear."""

    def __init__(self):
        self.__repr__ = lambda: "oski"
        self.__str__ = lambda: "this bear"

    def __repr__(self):
        return "Bear()"

    def __str__(self):
        return "a bear"


oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())
