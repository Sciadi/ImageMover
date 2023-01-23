"""Script to measure things while other Scripts executes"""

from time import time

# Measures Execution Time - ET - of func 
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        elapsed = end-start
        print(f'Execution Time of {func.__name__}: is {elapsed:.6f} seconds')
    return wrapper
        