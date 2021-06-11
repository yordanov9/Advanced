import functools
from datetime import time


def measure_time(func):
    @functools.wraps(func)
    def wrapper():
        start = time()
        result = func()
        end = time()
        print(f'{func.__name__} executed in {end - start} seconds')
        return result

    return wrapper
