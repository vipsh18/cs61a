def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    wrong_password_list = []

    def authenticated_withdrawal(amount, psw):
        nonlocal balance, password, wrong_password_list
        if len(wrong_password_list) >= 3:
            return f"Frozen account. Attempts: {wrong_password_list}"
        if password != psw:
            wrong_password_list.append(psw)
            return "Incorrect password"
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance

    return authenticated_withdrawal
