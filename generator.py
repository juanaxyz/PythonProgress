# def OodNumbers(size : int):
#     for n in range(size):
#         if n % 2 == 0:
#             yield n
            
# print(OodNumbers(100))
# for num in OodNumbers(10):
#     print(num)

import sys

nums_list = [x for x in range(1000000)]
nums_gen = (x for x in range(1000000))

print(sys.getsizeof(nums_list))  # Bisa ratusan MB
print(sys.getsizeof(nums_gen))   # Hanya beberapa puluh byte
