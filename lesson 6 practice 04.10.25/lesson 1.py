string = input("Enter a string: ")

count_letters = 0
count_numbers = 0
count_others = 0

for char in string:
    if char.isalpha():
        count_letters += 1
    elif char.isdigit():
        count_numbers += 1
    else:
        count_others += 1

print(f"Python 3.10! Вывод: Буквы: {count_letters}, Цифры: {count_numbers}, Остальные: {count_others}.")