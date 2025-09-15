a = float(input("1 сторона треугольника: "))
b = float(input("2 сторона треугольника: "))
c = float(input("3 сторона треугольника: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("«Equilateral» (равносторонний)")
    elif a == b or a == c or b == c:
        print("«Isosceles» (равнобедренный)")
    else:
        print("«Scalene» (разносторонний)")
else:
    print("Not a triangle")