def count_digits(num: int, n: int = 1) -> int:
    if len(str(num)) in (1, 0) or num <= 0:
        return n

    n += 1

    return count_digits(num // 10, n)


print(count_digits(123))