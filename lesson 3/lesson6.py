number = float(input("Enter number: "))

if number != 0:
    if number > 0:
        a = "Positive"
    else:
        a = "Negative"

    if number % 2 == 0:
        b = "even"
    else:
        b = "odd"

    print(a, b)
else:
    print("Zero")

