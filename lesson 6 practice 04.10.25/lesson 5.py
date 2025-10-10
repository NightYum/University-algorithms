string = input("Enter a string: ")

index_login = string.find("@almau.edu.kz")

print("Имя:", string[:index_login], "Домен:", string[index_login:])