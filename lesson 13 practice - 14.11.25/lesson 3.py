class BankWallet:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def add_money(self, amount):
        self.wallet += amount
        print(f"{self.name}, вы пополнили баланс на сумму {amount} тг. При пополнении баланс составляет: {self.wallet}")

    def get_money(self, amount):
        if self.wallet >= amount:
            self.wallet - amount
            print(f"{self.name}, вы сняли средства с баланса на сумме {amount}. Текущий баланс: {self.wallet}")
        else:
            print("Недостаточно денег")
    def current_balance(self):
        print(f"{self.name}, текущий баланс: {self.wallet}")

my_wallet = BankWallet("Михаил", 100)

my_wallet.get_money(110)
my_wallet.add_money(100)
my_wallet.current_balance()
my_wallet.get_money(110)