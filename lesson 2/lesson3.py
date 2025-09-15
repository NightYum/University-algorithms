a = int(input("Enter a number: "))

if a > 0:
    d = "Положительное"
else:
    d = "Отрицательное"

if a % 2 == 0:
    s = "четное"
else:
    s = "нечетное"

if a == 0:
    d = "Ноль"
    s = ""

print(d, s)

if a != 0:
    print("Положительное" if a > 0 else "Отрицательное", end=" ")
    print("четное" if a % 2 == 0 else "нечетное", end=" ")
else:
    print("Ноль")