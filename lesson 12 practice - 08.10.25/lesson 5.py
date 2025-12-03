def sum_dict(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

answer = sum_dict({'a': 1, 'b': 2}, {'c': 3, 'd': 4, "a": 5})
print(answer)


