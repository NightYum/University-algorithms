store = {'apple': 10, 'banana': 5, 'orange': 8, 'kiwi': 0}

sum = 0

for key, value in store.items():
    if value > 0:
        print(key, value)