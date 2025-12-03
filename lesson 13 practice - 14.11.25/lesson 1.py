class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

totoya = Car("Totoya", "Corolla", 2020)
print(totoya.mark, totoya.model, totoya.year)