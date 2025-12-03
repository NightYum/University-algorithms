def sum_shop(dict:dict) -> int:
    return sum(dict.values())

dict_shop = {"banana": 10, "apple": 5, "orange": 3}
print(sum_shop(dict_shop))