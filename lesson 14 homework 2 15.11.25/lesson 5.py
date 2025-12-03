class Movie:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def print_info(self):
        print(f"Фильм: {self.title}\nГод выхода: {self.year}\nАвтор: {self.author}")

my_movie = Movie("Интестеллар", "2014", "Me")
my_movie.print_info()