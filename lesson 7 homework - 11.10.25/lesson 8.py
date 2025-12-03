string_number = "10, 3, 8, 7".replace(", ", " ").split()

list_number = [int(string_number[i]) for i in range(len(string_number))]

clear_list_number = [list_number[i] for i in range(len(list_number)) if list_number[i] % 2 == 0]
print(clear_list_number)