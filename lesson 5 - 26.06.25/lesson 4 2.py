number = input("Enter a number: ")

count = 0
for i in range(0, 10):
    for j in number:
        if i == int(j):
            count += 1
    if count != 0:
        print(i, count)
    count = 0
