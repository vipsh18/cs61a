class Chef:
    """Doctests:

    >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
    >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
    >>> ramsay.cook()
    'Not enough ingredients!'
    >>> ramsay.serve()
    'No food to serve!'
    >>> ramsay.fetch_ingredients()     # 1 salt remaining
    "Fetched: ['meat', 'bbq sauce', 'salt']"
    >>> ramsay.cook()
    'Cooked steak!'
    >>> ramsay.serve()
    >>> Chef.finished
    ['steak']
    >>> albert.fetch_ingredients()     # 0 salt remaining
    "Fetched: ['egg', 'cheese', 'cream', 'salt']"
    >>> albert.cook()
    'Cooked quiche!'
    >>> albert.serve()
    >>> Chef.finished
    ['steak', 'quiche']
    >>> ramsay.fetch_ingredients()
    'No more salt!'
    """

    storage = {}
    finished = []

    def __init__(self, item, ingredients) -> None:
        self.item, self.ingredients = item, ingredients
        self.fetched, self.cooked = False, False
        for i in ingredients:
            Chef.storage[i] = 2

    def fetch_ingredients(self):
        for i in self.ingredients:
            if Chef.storage[i] == 0:
                return f"No more {i}!"
            Chef.storage[i] -= 1
        self.fetched = True
        return f"Fetched: {self.ingredients}"

    def cook(self):
        if not self.fetched:
            return "Not enough ingredients!"
        self.fetched, self.cooked = False, True
        return f"Cooked {self.item}!"

    def serve(self):
        if not self.cooked:
            return "No food to serve!"
        Chef.finished.append(self.item)
        self.cooked = False
