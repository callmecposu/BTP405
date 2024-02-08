import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'Function exec time: {time.perf_counter() - start: 0.4f}s')
        return res
    return wrapper

@timer_decorator
def mySum(rng):
    sum = 0
    for i in rng:
        sum += i
    return sum

@timer_decorator
def sleeper():
    time.sleep(2)

result = mySum(range(1,10000000))
print(f'Result: {result}')

sleeper()
