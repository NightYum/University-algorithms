shop = {"banana": 10, "apple": 20, "cucmber": 30}

item = input("enter item: ")
value = int(input("enter value: "))

if item in shop:
    print(f"Вы можете купить {item} по цене {shop[item]}, всего выйдет {shop[item]*value}.")
else:
    print("Такого продукта нет")