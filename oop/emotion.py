class Emotion:
    num = 0

    def __init__(self):
        Emotion.num += 1
        self.power = 5

    def feeling(self, other):
        if self.power == other.power:
            print("Together")
        elif self.power > other.power:
            self.catchphrase()
            other.catchphrase()
        else:
            other.catchphrase()
            self.catchphrase()


class Joy(Emotion):
    def catchphrase(self):
        print("Think positive thoughts")


class Sadness(Emotion):
    def catchphrase(self):
        print("I'm positive you will get lost")