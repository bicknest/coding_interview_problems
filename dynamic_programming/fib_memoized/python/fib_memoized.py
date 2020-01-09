import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
