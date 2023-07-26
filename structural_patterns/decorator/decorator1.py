#ciąg fbbonaciego rekursywnie
# 1, 1, 2, 3, 5 ,8, 13, 21
import time

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2) # dwa razy musi liczyć te same wyrazy ciągu fib

start = time.time()
fib(40)
stop = time.time()
print(stop - start)

import sys
sys.setrecursionlimit(10**9)

cache = dict()
fib_called = 0
def fib2(n):
    global fib_called
    fib_called += 1
    if n < 2:
        return 1
    if n in cache:
        return cache[n]
    result = fib2(n-1) + fib2(n-2)
    cache[n] = result
    return result


start = time.time()
fib2(3000)
stop = time.time()
print(stop - start)
print(stop-start)
print(fib_called)




