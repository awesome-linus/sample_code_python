def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib = fibonacci()

print(next(fib))

print(next(fib))

print(next(fib))

print("-" * 10)

list_comprehensions = [next(fib) for i in range(10)]

print(list_comprehensions)
