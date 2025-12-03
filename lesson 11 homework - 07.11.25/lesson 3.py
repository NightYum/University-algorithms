def sum_to_n(n):
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 1:
        raise ValueError("n должно быть >= 1")
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(3))