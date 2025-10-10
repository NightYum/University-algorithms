string = input("Enter a string: ")
reversed_string = string[::-1]

if reversed_string == string:
    print("Падиндром")
else:
    print("Не палиндром")