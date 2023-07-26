def memorize(fn):
    cache = dict()
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapper

@memorize
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2) 


@memorize
def factorial(n):
    if n < 2:
        return 1
    product = 1
    for i in range(2,n+1):
        product *= i
    return product

@memorize
def rec_factorial(n):
    if n < 2:
        return 1
    return n * rec_factorial(n-1)


print(fib(300))