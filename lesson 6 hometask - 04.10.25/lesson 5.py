string = "HHH eeee eeee eeeeeeee"
list_string = string.split()
dict_len_string = {}

for i in list_string:
    dict_len_string[len(i)] = i


print(min(dict_len_string.keys()), max(dict_len_string.keys()))