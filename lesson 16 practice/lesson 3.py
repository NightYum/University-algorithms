class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 1,8 + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def update(self, celsius):
        self.celsius = celsius

t = Temperature(25)
print(t.to_fahrenheit())
print(t.to_kelvin())
t.update(5)
print(t.celsius)
print(t.to_fahrenheit())
print(t.to_kelvin())