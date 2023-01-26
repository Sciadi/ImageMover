"""Script to measure exec time of wrapped function"""

from time import time

def time_it(func):
    """Measures Execution Time - ET - of func 

    Args:
        func (func): function to be wrapped
    """
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        elapsed = end-start
        print(f'Execution Time of {func.__name__}: is {elapsed:.6f} seconds')
    return wrapper
        