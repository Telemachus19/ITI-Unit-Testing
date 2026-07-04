def factorial(n):
    if type(n) is not int or n < 0  : return None;
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact