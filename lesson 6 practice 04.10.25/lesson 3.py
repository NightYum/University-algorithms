string = "Python is a powerful programming language"
list_string = string.split()

for i in list_string:
    if len(i) > 4:
        print(i)