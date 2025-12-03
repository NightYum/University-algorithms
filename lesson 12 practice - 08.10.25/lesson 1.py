def avg(dict: dict) -> dict:
    new_dict = {}
    for item, value in dict.items():
        new_dict[item] = sum(value) / len(value)
    return new_dict

students_dict = {"Mikhail": [10, 5, 2, 4, 8],
                 "Supermen": [10, 10, 10, 2]}

print(avg(students_dict))