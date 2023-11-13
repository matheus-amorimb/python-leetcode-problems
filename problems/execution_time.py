import time

def timing_decorator(func):
    def inner(*args, **kwargs):
        init = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        total_time = (end - init) * 1000
        print(f'({func.__name__}) Run time: {total_time}ms')
        return result    
    return inner