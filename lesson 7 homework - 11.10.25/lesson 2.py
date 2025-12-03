string = "Big brown bear, black bird, hello world"
char = input("Enter a character: ")

clear_string = string.replace(",", "").replace(".", "")
list_string = clear_string.split()

new_list = []

for i in list_string:
    if i[0].lower() == char.lower():
        new_list.append(i)

print(new_list)