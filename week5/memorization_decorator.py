import time

cache = dict()

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'Function exec time: {time.perf_counter() - start: 0.4f}s')
        return res
    return wrapper

def argument_wrapper(func_name):
    def memorization_decorator(func):
        def wrapper(*args, **kwargs):
            funcCache = cache.get(func_name)
            callCache = None
            if funcCache:
                callCache = funcCache.get(tuple(*args, **kwargs))
            print(f'FuncCache: {funcCache} \nCallCache: {callCache}')
            if callCache:
                return callCache
            result = func(*args, **kwargs)
            if not funcCache:
                cache[func_name] = dict()
                funcCache = cache.get(func_name)
            cache[func_name][tuple(*args, **kwargs)] = result
            return result
        return wrapper
    return memorization_decorator

@timer_decorator
@argument_wrapper(func_name='mySum')
def mySum(rng):
    sum = 0
    for i in rng:
        sum += i
    return sum

def myAvg(rng):
    return mySum(rng) / len(rng)


# mySum(range(1,50000000))
# mySum(range(1,50000000))

mySum(range(1,10))
mySum(range(1,10))
myAvg(range(1,10))

