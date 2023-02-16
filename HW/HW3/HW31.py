import time

def cache(func):
    saved = {}
    def wrapper(*args):
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return wrapper

@cache
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def timer_process(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{func.__name__}({args}) = {result}, executed in {execution_time:.6f} seconds")

def slow_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def slow_fibonacci(n):
    if n <= 1:
        return n
    prev1 = 0
    prev2 = 1
    result = 0
    for i in range(2, n+1):
        result = prev1 + prev2
        prev1 = prev2
        prev2 = result
    return result

# Test the functions with some input values
timer_process(factorial, 5)
timer_process(factorial, 10)
timer_process(factorial, 20)
timer_process(fibonacci, 5)
timer_process(fibonacci, 10)
timer_process(fibonacci, 20)

# Compare with the slow versions
timer_process(slow_factorial, 5)
timer_process(slow_factorial, 10)
timer_process(slow_factorial, 20)
timer_process(slow_fibonacci, 5)
timer_process(slow_fibonacci, 10)
timer_process(slow_fibonacci, 20)

# output

# factorial(5) = 120, executed in 0.000002 seconds
# factorial(10) = 3628800, executed in 0.000002 seconds
# factorial(20) = 2432902008176640000, executed in 0.000003 seconds
# fibonacci(5) = 5, executed in 0.000002 seconds
# fibonacci(10) = 55, executed in 0.000003 seconds
# fibonacci(20) = 6765, executed in 0.000110 seconds
# slow_factorial(5) = 120, executed in 0.000003 seconds
# slow_factorial(10) = 3628800, executed in 0.000019 seconds
# slow_factorial(20) = 2432902008176640000, executed in 0.000050 seconds
# slow_fibonacci(5) = 5, executed in 0.000005 seconds
# slow_fibonacci(10) = 55, executed in 0.000001 seconds
# slow_fibonacci(20) = 6765, executed in 0.001596 seconds
