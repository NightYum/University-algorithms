number = int(input("Enter a number: "))
sum_number = 0

for i in range(number+1):
    if i % 7 == 0:
        sum_number += i

print(sum_number)