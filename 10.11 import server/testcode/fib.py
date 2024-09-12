print('im fib')


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# python3 -m http.server 15000