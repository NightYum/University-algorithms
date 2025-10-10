numbers = [12, 45, 3, 67, 23, 89, 5]

# print(min(numbers), max(numbers))

# min_number = 1000
# max_number = 0

min_number = numbers[0]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
        # if number < min_number:
        #     min_number = number

    if number < min_number:
        min_number = number

print(min_number, max_number)