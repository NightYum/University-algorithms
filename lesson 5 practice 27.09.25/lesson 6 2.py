string = input("Enter a string: ")

count_char = 0
itteration_char = []

for char in string:
    if char not in itteration_char:
        for char2 in string:
            if char == char2:
                count_char += 1
        print(char, count_char)
        count_char = 0
        itteration_char.append(char)
