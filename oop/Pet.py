class Pet:
    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + "says woof!")


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        # Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.
        >>> Cat('Thomas','Tammy').talk()
        Thomas says meow!
        """
        print(f"{self.name} says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches
        zero,'is_alive' becomes False. If this is called
        after lives has reached zero, print out that the cat
        has no more lives to lose."""
        if not self.is_alive:
            return "No more lives to lose!"
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False


class NoisyCat(Cat):
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic','James').talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()

    def __repr__(self):
        """The interpreter-readable representation of
        a NoisyCat
        >>> muffin = NoisyCat('Muffin','Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin','Catherine')"
        >>> muffin
        NoisyCat('Muffin','Catherine')
        """
        return f"{type(self).__name__}({repr(self.name)},{repr(self.owner)})"