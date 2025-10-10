cities = ["New York", "London", "Tokyo", "Berlin", "Paris", "Dubai"]

for city in cities:
    for char in city:
        print(char.upper(), end="")
    print(end="\n")