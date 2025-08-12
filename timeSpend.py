import random
import time
from data_structure_and_algorithms.quick_sort import quick_sort 
from data_structure_and_algorithms.buble_sort import buble_sort

def timespend(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        
        value = function(*args, **kwargs)
        
        after = time.time()
        
        timeSpended = after - before
        
        print(f"time spended for function {function.__name__} = {timeSpended}")
        return value
    return wrapper

numbers = []

numbers = [random.randint(1,10000) for _ in range (10000)]
# print(f"list acak : {numbers}")
@timespend
def algorithm(name):
    print(f"algoritma {name}")
    return quick_sort(numbers)

algorithm("quick sort")