info = {"name": "Aigerim", "age": 21, "city": "Almaty"}
string = "Меня зовут {name}, мне {age} год, я живу в {city}!"
print(string.format_map(info))
