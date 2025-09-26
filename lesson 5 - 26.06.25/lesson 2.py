number = int(input("Enter a number: "))
result_number = 1

for i in range(1, number + 1):
    if i % 3 == 0:
        result_number *= i

print(result_number)
