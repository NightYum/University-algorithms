def count_even_odd(numbers_list):
    even = 0
    odd = 0
    for i in numbers_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(even, odd)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_even_odd(numbers_list)