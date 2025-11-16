def fibonacciGenerator(max):
    a = 0
    b = 1
    while a < max:
        if a % 2 == 0:
            yield a
        a, b = b, a + b

print(sum(fibonacciGenerator(4000000)))