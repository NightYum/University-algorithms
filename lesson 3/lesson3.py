number = int(input("Введите целое число: "))

if number % 2 == 0 and number % 3 == 0:
    print("Divisible by 2 and 3")
elif number % 2 == 0:
    print("Divisible by 2")
elif number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")