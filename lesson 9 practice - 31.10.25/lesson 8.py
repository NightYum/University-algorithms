def change_list(lst):
    lst[0] = "Новый элемент"
    print(lst)

def change_string(s):
    s = s.lower()
    print(s)

number_list = [1, 2, 3, 4, 5]
string = "Это будет новой строкой"

change_list(number_list)
change_string(string)