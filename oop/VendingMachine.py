class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity, self.funds = 0, 0

    def vend(self):
        if self.quantity <= 0:
            return "Inventory empty. Restocking required."
        if self.funds < self.price:
            return f"You must add ${self.price - self.funds} more funds."
        self.quantity -= 1
        fmp = self.funds - self.price
        self.funds = 0
        if fmp > 0:
            return f"Here is your {self.name} and ${fmp} change."
        return f"Here is your {self.name}."

    def add_funds(self, amount):
        if self.quantity <= 0:
            return f"Inventory empty. Restocking required. Here is your ${amount}."
        self.funds += amount
        return f"Current balance: ${self.funds}"

    def restock(self, stock):
        self.quantity += stock
        return f"Current {self.name} stock: {self.quantity}"