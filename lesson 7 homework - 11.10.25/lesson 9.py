def rotate_list(data_list: int, step: int = 2) -> list:
    new_list = [9] * len(data_list)

    for i in range(len(data_list)):
        if len(data_list) > i + step:
            new_list[i+step] = data_list[i]
        else:
            new_list[i+step-len(data_list)] = data_list[i]

    print(new_list)

data_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data_list)
rotate_list(data_list, 2)