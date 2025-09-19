i = int(input("Enter a number: "))
j = 1
count_number = 0
while j <= i:
    if i % j == 0:
        count_number += 1
    j += 1
if count_number == 2:
    print("Число простое")
else:
    print("Число не простое")
