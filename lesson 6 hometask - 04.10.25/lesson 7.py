string = "HELLO WORLD hello world".lower()
count_dict = {}

for char in string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
sorted_dict_count = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(len(sorted_dict_count)):
    print(sorted_dict_count[i][0], sorted_dict_count[i][1])