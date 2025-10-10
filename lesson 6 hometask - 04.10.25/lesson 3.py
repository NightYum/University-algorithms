string = input("Enter a string: ")

count_letters = 0
count_numbers = 0
count_spaces = 0

for char in string:
    if char.isalpha():
        count_letters += 1
    elif char.isdigit():
        count_numbers += 1
    elif char.isspace():
        count_spaces += 1

print(f"Буквы: {count_letters}, Цифры: {count_numbers}, Пробелы: {count_spaces}.")