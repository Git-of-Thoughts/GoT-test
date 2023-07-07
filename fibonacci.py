def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        a, b = 0, 1
        for _ in range(n-2):
            a, b = b, a + b
            fib.append(b)
        return fib

print(fibonacci(10))        return fib

print(fibonacci(10))