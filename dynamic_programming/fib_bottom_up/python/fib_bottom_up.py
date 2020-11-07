def fib_bottom_up(n):
    if n < 0:
        return "No negative numbers in series"
    
    if n == 0:
        return 0
    
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib[n - 1]
