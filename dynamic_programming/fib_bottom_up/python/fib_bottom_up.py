def fib_bottom_up(n):
    if n < 0:
        return "No negative numbers in series"
    
    if n == 0:
        return 0
    
    fib = []
    for i in range(0, n + 1):
        if i <= 1:
            fib.append(1)
        else:
            fib.append(fib[i -1] + fib[i - 2])
    
    return fib[n - 1]
