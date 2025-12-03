def pow2(n):
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Аргумент должен быть >= 0")
    if n == 0:
        return 1
    print(n, n*2)
    return 2 * pow2(n - 1)

print(pow2(3))