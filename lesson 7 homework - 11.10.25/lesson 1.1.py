string = input("Enter a string: ")

clear_string = string.replace(",", "").replace(".", "")
list_string = clear_string.split()
print(len(list_string))