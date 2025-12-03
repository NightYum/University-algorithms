try:
    user_input = int(input("Enter a number: "))
except ValueError:
    raise "Ошибка: введите число!"

print(user_input**2)