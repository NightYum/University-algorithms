from random import randint

random_list = [randint(1, 20) for i in range(10)]
print(random_list)
print("Уникальных чисел: ", len(set(random_list)))
print("Кол-во повторяющихся чисел", len(random_list) - len(set(random_list)))