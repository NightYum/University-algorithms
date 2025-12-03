class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def promote(self, new_position, salary_increase):
        self.position = new_position
        self.salary += salary_increase

    def get_salary(self):
        return self.salary * 12

emp = Employee('Mikhail', "SE", 2000)

emp.promote("Main SE", 1000)
print(emp.get_salary())