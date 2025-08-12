from random import randint

def buble_sort(list_items: list):
    for i in range(len(list_items)):
        for j in range(len(list_items)-1):
            if list_items[j] > list_items[j+1]:
                temp = list_items[j]
                list_items[j] = list_items[j+1]
                list_items[j+1] = temp
    # print(list_items)
    return list_items
    
if __name__ == "__main__":
    numbers = []
    for n in range(10):
        numbers.append(randint(1,100))
            
    buble_sort(numbers)