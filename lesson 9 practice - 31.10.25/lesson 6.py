def outer(a):
    def inner(a):
        return a ** 3
    print(inner(a))

outer(3)