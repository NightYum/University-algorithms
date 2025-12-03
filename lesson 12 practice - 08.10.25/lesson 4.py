def filter(d, t):
    return {key: value for key, value in d.items() if value >= t}

data = {"a":5, "b":6, "c":7, "d":2}
print(filter(data, 4))