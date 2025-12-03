def min_recursive(list: list) -> None | int | str:
    if len(list) == 0:
        raise ValueError("Пустой список")
    sub_min = min_recursive(list[1:])
    return list[0] if list[0] < sub_min else sub_min

print(min_recursive([2, 3, 3, 1, 5]))
print(min_recursive([5, 3, 3, 5, 5, 10, 11, 15, 1]))
print(min_recursive([]))