string = input("Enter a string: ")
count_upper_letters = 0
count_lower_letters = 0
count_digits = 0
not_boolean_space = True

for char in string:
    if char.isupper():
        count_upper_letters += 1
    elif char.islower():
        count_lower_letters += 1
    elif char.isdigit():
        count_digits += 1
    elif char == ' ':
        not_boolean_space = False


if not_boolean_space and len(string) >= 10 and count_upper_letters >= 2 and count_lower_letters >= 2 and count_digits >= 1:
    print("Password is correct")
else:
    print("Password is incorrect")