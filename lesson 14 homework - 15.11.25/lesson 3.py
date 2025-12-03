class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount

    def get_balance(self):
        return self._balance

my_account = Account("Mikhail", 100)
print(my_account.get_balance())
my_account.withdraw(90)
print(my_account.get_balance())
my_account.withdraw(100)
print(my_account.get_balance())
my_account.deposit(123)
print(my_account.get_balance())