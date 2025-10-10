string = input("Enter a string: ")
list_string = string.split()
for i in list_string:
    if i.istitle():
        print(i)