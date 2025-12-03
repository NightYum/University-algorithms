class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return (self.title, self.author, self.year)

my_book = Book("Mathematics", "Me", "1999")
my_book_info = my_book.get_info()
print(f"Название книги: {my_book_info[0]}\nАвтор: {my_book_info[1]}\nГод: {my_book_info[2]}")