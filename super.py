class Vehicle:
    def __init__(self):
        self.drive = input('Drive?: ')
        self.wheels = input('How many wheels?: ')
        self.seat = input('How many seats?: ')
        self.move = input('Movement: ')

class Car(Vehicle):
    kind = input('Car type: ')
    def __init__(self):
        super().__init__()
        self.color = input('Favorite color: ')

    def convertible(self, full='fully Convertible'):
        self.full = full
        print(f'{Car.kind} is a {self.full}')


    def __str__(self):
        return  self.drive + " " + self.wheels + " " +self.seat + " " + self.move
        

cab_1 = Car()
print(cab_1)
# print(cab_1.drive)
# print(cab_1.wheels)
# print(cab_1.seat, cab_1.move)
# print(Car.kind)
# print(cab_1.color)
# cab_1.convertible()