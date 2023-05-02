def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    num1 = 1
    num2 = 0
    i = 0
    while i < n:
        num3 = num2
        num2 = num1 + num2
        num1 = num3
        fib.append(num3)
        i += 1
    return fib
print(n)