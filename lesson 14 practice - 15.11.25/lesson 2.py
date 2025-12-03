def open_txt(filename: str):
    try:
        with open(filename) as f:
            all_words = f.read().split()
            count_words = len(all_words)
    except FileNotFoundError:
        count_words = -1

    if count_words == 0:
        print(f"Файл {filename} пуст")
    elif count_words == -1:
        print(f"Файл {filename} не найден")
    else:
        print("Кол-во слов в файле:", count_words)

open_txt("story.txt")
open_txt("story1.txt")
open_txt("nonfoundfile.txt")