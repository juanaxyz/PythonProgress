import statistics
import random 

def get_random_numbers(n: int):
    list_num = []
    for _ in range(n):
        list_num.append(random.randint(1,100))
    return list_num

def quick_sort(number_list: list):
    smaller_list = []
    greater_list = []
    pivot_list = []
    
    if len(number_list) <=1:
        return number_list
    pivot = statistics.median(
        [
            number_list[0],
            number_list[len(number_list) //2],
            number_list[-1]
        ]
    )
    
    
    for n in number_list:
        if n < pivot:
            smaller_list.append(n)
        elif n == pivot:
            pivot_list.append(n)
        else:
            greater_list.append(n)
    
    return (quick_sort(smaller_list) + pivot_list + quick_sort(greater_list))
            

if __name__ == "__main__":
    numbers = get_random_numbers(10)
    print(quick_sort(numbers))
