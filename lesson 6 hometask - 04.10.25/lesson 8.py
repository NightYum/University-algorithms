string = input("Enter a string: ")

count_upper = 0
count_lower = 0

for char in string:
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1

all_count = count_upper + count_lower
percent_upper = count_upper / all_count
percent_lower = count_lower / all_count

print(percent_upper, percent_lower)