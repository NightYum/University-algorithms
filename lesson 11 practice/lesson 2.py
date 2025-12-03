def sum_list(list: list, n = 0) -> int:
    if len(list) == 0:
        return n

    try:
        n += list[0]
    except TypeError:
        return sum_list(list[1:], n)

    return sum_list(list[1:], n)


print("result:", sum_list([1, 2, 3, "a", 1]))
print("result:", sum_list([3]))
print("result:", sum_list([1, 2, "b", 3, "a"]))