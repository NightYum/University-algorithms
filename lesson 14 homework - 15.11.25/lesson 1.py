class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}({self.year})")

book1 = Book("Война и мир", "Л. Толстой", "1869")
book1.print_info()