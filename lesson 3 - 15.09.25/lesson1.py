str_number = input("Введите двухзначное число: ")

a = int(str_number[0])
b = int(str_number[1])
c = a + b

if c > 10:
    print("Big sum")
elif c < 10:
    print("Small sum")
elif c == 10:
    print("Perfect sum")