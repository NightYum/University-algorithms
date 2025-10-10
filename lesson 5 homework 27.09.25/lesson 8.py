string = input("Enter a string: ")
len_string = len(string)

for i in range(len_string-1, -1, -1):
    print(string[i], end="")