try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a / b)
except ZeroDivisionError:
    print("Нельзя делить на ноль")
else:
    print("Код завершен без ошибки")
finally:
    print("Код завершен")