class Employee:
    count = 0
    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.count += 1

    @classmethod
    def total_emplyees(cls):
        return cls.count

e1 = Employee("Михаил", "Директор")
e2 = Employee("Михаил", "Директор")
e3 = Employee("Михаил", "Директор")

print(Employee.total_emplyees())