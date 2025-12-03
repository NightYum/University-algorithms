class Shop:
    def __init__(self, name: str, item: dict):
        self.name = name
        self.item = item

    def get_info(self):
        if self.item == {}:
            return "Нет товаров"
        return self.item

    def add_item(self, item):
        self.item.update(item)

magnum = Shop("Magnum", {})

print(magnum.get_info())
magnum.add_item({"banana": 100})
magnum.add_item({"kiwi": 200})
print(magnum.get_info())