text = "Python is a powerful programming language"
count_symbol = 0
count_phrase = 0
count_phrase_length = 0

for symbol in text:
    if symbol != " ":
        count_symbol += 1
    if symbol == " ":
       11 count_phrase += 1
        count_symbol = 0

    if count_symbol == 4:
        count_phrase_length += 1

print(count_phrase_length)