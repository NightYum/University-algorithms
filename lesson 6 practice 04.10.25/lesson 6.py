string = input("Введите число: ")
sum_number = 0

for char in string:
    if int(char) % 2 == 0:
        sum_number += int(char)

print("Сумма", sum_number)