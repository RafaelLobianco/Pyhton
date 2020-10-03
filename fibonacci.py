def fib(i):
    if i <= 1:
        return i
    if i ==2:
        return 1
    return fib(i-1) + fib(i-2)

