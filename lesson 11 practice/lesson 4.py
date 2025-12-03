def find_element(list: list, element: [int, str], n: int = 0) -> int:
    if len(list) == 0:
        return -1
    if len(list) == 1:
        return list[0]
    if list[n] == element:
        return n
    n+=1
    return find_element(list, element, n)

print(find_element([1, 2, 3, "h", "j"], "h"))