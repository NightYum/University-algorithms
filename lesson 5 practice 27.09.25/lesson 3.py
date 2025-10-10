number = int(input("Enter a number: "))

print("Четные")
for i in range(number+1):
    if i % 2 == 0:
        print(i)

print("Нечетные")
for i in range(number+1):
    if i % 2 != 0:
        print(i)
