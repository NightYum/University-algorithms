list_string = "Hello World! heLLo World!".lower().split()

new_dict = {}

for i in list_string:
    if i in new_dict:
        new_dict[i] = new_dict[i] + 1
    else:
        new_dict[i] = 1

print(new_dict)