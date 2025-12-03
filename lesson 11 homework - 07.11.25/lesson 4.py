def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Аргумент должен быть строкой")
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("Hello"))
