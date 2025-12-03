class Phone:
    def __init__(self, mark: str, model: str, price: float):
        self.mark = mark
        self.model = model
        self.price = price

    def print_info(self):
        print(f"Телефон: {self.mark}\nМодель: {self.model}\nЦена: {self.price}")

my_phone = Phone("Xiaomi", "Ultra pro max iphone 22", 0.99)
my_phone.print_info()