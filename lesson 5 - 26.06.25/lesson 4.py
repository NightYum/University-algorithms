
number = input("Enter a number: ")

dict_number = {}

for i in range (len(number)):
    if number[i] in dict_number:
        dict_number[number[i]] = dict_number[number[i]] + 1
    else:
        dict_number[number[i]] = 1


print(dict_number)