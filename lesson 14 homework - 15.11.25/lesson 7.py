class Engine:
    def __init__(self, power):
        self.power = power

class Car(Engine):
    def  car_info(self):
        print(self.power)

my_car = Car(150)
my_car.car_info()