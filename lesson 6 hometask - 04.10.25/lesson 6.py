string = input("Enter a string: ")
count_letters = 0
count_digits = 0
boolean_space = False

for char in string:
    if char.isalpha():
        count_letters += 1
    elif char.isdigit():
        count_digits += 1
    elif char == ' ':
        boolean_space = True

print(count_letters, count_digits, boolean_space, len(string))
if not boolean_space and  15 > len(string) > 6 and count_letters >= 1  and count_digits >= 1:
    print("Password is correct")
else:
    print("Password is incorrect")