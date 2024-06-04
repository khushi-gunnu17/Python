import time

def cache(func) :
    cache_value = {}
    print(cache_value)
    # It is easy to access values in a dictionary

    def Wrapper(*args) :
        if args in cache_value :
            return cache_value[args]
    
        result = func(*args)
        cache_value[args] = result
        return result
    
    return Wrapper

@cache
def long_running_function(a, b) :
    time.sleep(4)
    return a + b

print(long_running_function(5, 6))
print(long_running_function(5, 6))
print(long_running_function(5, 10))
print(long_running_function(5, 10))
print(long_running_function(5, 11))