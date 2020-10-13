def almost_double_factorial(n):
    if n == 0:
        func = 1
    else:
        func = 1
        for i in range(1, n+1, 2):
            func = func * i
    return func