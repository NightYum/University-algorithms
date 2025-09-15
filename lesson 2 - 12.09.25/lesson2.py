a = float(input("Enter a temperature: "))

if a < -10:
    print("Слишком холодно, оставайтесь дома!")
elif a >= -10 and a <= 0:
    print("Наденьте тёплое пальто")
elif a >= 1 and a <= 20:
    print("Возьмите куртку")
elif a >= 21 and a <= 30:
    print("Футболки достаточно")
elif a > 30:
    print("Пейте больше воды, на улице жарко!")