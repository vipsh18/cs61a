class CircularBuffer:
    """
    >>> buffer = CircularBuffer(3)
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('a')
    >>> buffer.remove()
    'a'
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('b')
    >>> buffer.append('c')
    >>> buffer.append('d')
    >>> buffer.append('e')
    Buffer capacity exceeded
    >>> buffer.remove()
    'b'
    >>> buffer.remove()
    'c'
    >>> buffer.remove()
    'd'
    >>> buffer.remove()
    Buffer is empty
    """

    def __init__(self, n):
        self.array = [None] * n  # list of length n
        self.n = n
        self.start = 0
        self.end = 0

    def append(self, elem):
        if self.end - self.start == self.n:
            print("Buffer capacity exceeded")
        else:
            self.array[self.end % self.n] = elem
            self.end += 1

    def remove(self):
        if self.start == self.end:
            print("Buffer is empty")
        else:
            elem = self.array[self.start % self.n]
            self.start += 1
            return elem

    def showBuffer(self):
        print([i for i in self.array])