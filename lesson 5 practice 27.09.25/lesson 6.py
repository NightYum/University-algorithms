string = input("Enter a string: ")

dict_char = {}

for char in string:
    if char in dict_char:
        dict_char[char] = dict_char[char] + 1
    else:
        dict_char[char] = 1
  
print(dict_char)