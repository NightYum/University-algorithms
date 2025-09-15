number = int(input("Введите кол-во минут разговора: "))

if 0 <= number <= 100:
    print("Стоимость", number * 5, "тг.")
elif 101 <= number <= 300:
    print("Стоимость", number * 4, "тг.")
elif number > 300:
    print("Стоимость", number * 3, "тг.")