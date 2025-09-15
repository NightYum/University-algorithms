






a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите действие над числами: ")

if c in "+-*/":
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
else:
    print("Неверная операция")
