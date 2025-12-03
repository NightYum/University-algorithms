n = int(input("Input a number: "))

def factorial(n):
    if n == 1:
        return 1
    else:
        try:
            return n * factorial(n-1)
        except:
            return 0

answer = factorial(n)
print(answer)