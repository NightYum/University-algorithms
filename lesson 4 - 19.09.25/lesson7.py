secret_number = 7
while True:
    number = int(input("Write number here: "))
    if number == secret_number:
        print("Correct number")
        break
    if number > secret_number:
        print("Too high")
    elif number < secret_number:
        print("Too low")