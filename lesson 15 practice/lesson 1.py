def limited_sum(a, b, limit):
    try:
        if not (isinstance(a, int) or isinstance(limit, float)):
            raise TypeError
        result = a + b
        if result > limit:
            raise Exception("Limit exceeded")
        return result
    except TypeError:
        print("Invalid argument")

result = limited_sum(1, 10, 100)
print(result)