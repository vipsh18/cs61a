class Account:
    interest = 0.02

    def __init__(self, holder, balance=0):
        self.balance = balance
        self.holder = holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_holder(self):
        return self.holder


class CheckingAccount(Account):
    """A bank account that charges for withdraws
    >>> ch = CheckingAccount("Tim")
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


class Bank:
    """A bank *has* accounts
    >>> bank = Bank()
    >>> john = bank.open_account("John", 10)
    >>> jack = bank.open_account("Jack", 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """

    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1

    def list_accounts(self):
        for num, acc in enumerate(self.accounts):
            print(f"Account {num} =>")
            print(f"\tHolder: {acc.get_holder()}")
            print(f"\tBalance: {acc.get_balance()}")


class SavingsAccount(Account):
    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar


# deal = AsSeenOnTVAccount("Avast")
# print(deal.get_balance())
# print(deal.deposit(20))
# print(deal.withdraw(5))

# bank = Bank()
# john = bank.open_account("John", 10)
# jack = bank.open_account("Jack", 5, CheckingAccount)
# bank.pay_interest()
# bank.list_accounts()