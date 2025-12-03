string = "Apple, apple! Banana"

clear_string = string.replace(",", "").replace(".", "").replace("!", "")

lower_string = clear_string.lower()

set_string = set(lower_string.split())

list_string = list(set_string)

sorted_list_string = sorted(list_string)

print(sorted_list_string)