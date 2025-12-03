class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def add_mileage(car, mileage):
        car.mileage += mileage

    def get_info(self):
        print(f"{self.brand} {self.model} {self.year} {self.mileage}")

car1 = Car("Nissan",  "GTR", 2007, 70000)

car1.add_mileage(2000)
car1.get_info()