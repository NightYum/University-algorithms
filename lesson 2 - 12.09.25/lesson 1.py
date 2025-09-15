a = float(input("Enter a number: "))

if a <= 100 and a >= 90:
    print("Excellent")
elif a <= 89 and a >= 75:
    print("Good")
elif a <= 74 and a >= 50:
    print("Satisfactory")
elif a <= 49 and a >= 0:
    print("Fail")
else:
    print("Invalid score")
