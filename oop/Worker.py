class Worker:
    greeting = "Sir"

    def __init__(self):
        self.elf = Worker

    def work(self):
        return self.greeting + ", I work"

    def __repr__(self):
        return Burg.greeting


class Burg(Worker):
    greeting = "Peon"

    def work(self):
        print(Worker.work(self))
        # print(super().work())
        return "I gather wealth"


jack = Worker()
john = Burg()
jack.greeting = "Maam"
