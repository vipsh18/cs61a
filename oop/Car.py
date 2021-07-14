class Car:
    num_wheels = 4

    def __init__(self, color, make):
        self.color = color
        self.make = make
        self.gas = 10
        print("New car on the raod!")

    def drive(self):
        if self.gas == 0:
            return "Can't drive on an empty tank!"
        self.gas -= 5
        return "Vroom vroom"

    def park(self):
        if self.num_wheels >= 4:
            return "In between white lines!"
        else:
            return "Oof, you getter find a new spot!"

    def paint(self):
        return f"Added new {self.color} paint to the {self.make}!"

    def refill_gas_tank(self):
        self.gas = 10


class Motorcycle(Car):
    num_wheels = 2