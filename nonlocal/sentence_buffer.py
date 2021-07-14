def sentence_buffer():
    """Returns a function that will return entire sentences when it
    receives a string that ends in a period.

    >>> buffer = sentence_buffer()
    >>> buffer("This")
    >>> buffer("is")
    >>> buffer("Spot.")
    'This is Spot.'
    >>> buffer("See")
    >>> buffer("Spot")
    >>> buffer("run.")
    'See Spot run.'
    """
    sentence = ""

    def save_this_word(word):
        nonlocal sentence
        sentence += f"{word} "
        if word[-1] == ".":
            result, sentence = sentence, ""
            return result.strip()

    return save_this_word