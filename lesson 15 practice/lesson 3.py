def diff(n):
    try:
        if not isinstance(n, int):
            raise TypeError('n must be an integer')
        if n < 1:
            raise Exception('Invalid argument')
        if n == 1:
            return 1
        return n - diff(n - 1)
    except TypeError:
        print('Invalid argument')

result = diff(5)
print(result)