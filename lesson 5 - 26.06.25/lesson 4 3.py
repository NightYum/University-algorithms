str_number = input("Enter a number: ")
count = 0

set_number = set()
for number in str_number:
    set_number.add(number)

sort_set_number = sorted(set_number)

for number in sort_set_number:
    for i in str_number:
        if i == number:
            count += 1
    print(number, count)
    count = 0