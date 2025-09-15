number = int(input("Введите сумму покупки: "))

if number <= 5000:
    print("Скидки нет")
elif 10000 >= number > 5000:
    print("Скидка составляет", number * 0.05, "тг.")
elif number > 10000:
    print("Скидка составляет", number * 0.1, "тг.")