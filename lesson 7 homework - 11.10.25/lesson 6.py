number_list =[5, 3, 5, 2, 4]
clear_number_list = list(set(number_list))
pre_max_number = 0
max_number = 0

for i in clear_number_list:
    if max_number < i:
        pre_max_number = max_number
        max_number = i

print(pre_max_number, max_number)
