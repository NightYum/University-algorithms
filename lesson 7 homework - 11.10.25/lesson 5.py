def remove_short_words(text: str, length: int) -> str:
    new_string = ""
    for word in text.split():
        if len(word) > length:
            new_string += " " + word

    return new_string

user_text = input("Enter user text:").lower()
string_short_word = remove_short_words(user_text, 4)
print(string_short_word)