class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, name, price):
        self.items.append((name, price))
        self.total_price += price

    def summary(self):
        print("Ваш заказ:")
        for item in self.items:
            print("-", item[0], ":", item[1], "тг")
        print("Итого:", self.total_price, "тг")

order = Order()
order.add_item("Картошка", 210)
order.add_item("Бургер", 400)
order.add_item("Кола", 150)

order.summary()