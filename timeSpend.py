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
        
        print(f"time spended for function is {timeSpended}")
        return value
    return wrapper

numbers = []

numbers = [random.randint(1,10000) for _ in range (10000)]
# print(f"list acak : {numbers}")
@timespend
def algorithmqs():
    print(f"algoritma quick sort")
    quick_sort(numbers)
    
@timespend
def algorithmbs():
    print("algoritma buble sort ")
    buble_sort(numbers)
    
algorithmqs()
algorithmbs()