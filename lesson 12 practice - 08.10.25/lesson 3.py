def count_words(text):
    text = text.replace(",", " ").lower().split()
    new_dict = {}
    for word in text:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    return new_dict

print(count_words("Hello good good, hello, bye"))