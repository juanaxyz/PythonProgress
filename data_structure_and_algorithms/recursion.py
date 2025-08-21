import time

def countdown(n: int):
    if n == 0:
        print("boom!!!")
        return
        
    print(f"you have {n} sec left")
    time.sleep(1)
    countdown(n-1)
    
    
countdown(1)

##########

def factorial(n: int):
    return 1 if n ==1 else n*factorial(n-1)
    
print(factorial(5))

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

def count_all(list_item: list):
    count = 0
    print(f"list = {list_item}")
    for item in list_item:
        if isinstance(item,list):
            count += count_all(list_item=item)
        else:
            count +=1
    return count

print(count_all(names))


# palindrom
def check_palindrom(word: str):
    return True if word[0] == word[::-1] else False

def check_palindrom_recursive(word: str):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and check_palindrom_recursive(word[1:-1])
    
print(("foo")[::-1]) #::-1 itu slicing stepnya 1 dari belakang
print(check_palindrom("foo"))

words = input("masukkan kata : ")

print(check_palindrom_recursive(words))
