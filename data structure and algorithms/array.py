'''
array dan list merupakan 2 hal yang mirip namun berbeda
list = bisa berisi berbagai macam tipe data
array = hanya bisa menyimpan nilai yang memiliki tipe data yang sama (sesuai dengan yang di tentukan saat membuat array)


a=array.array(data type,value list) #general usage
a=arr.array(data type,value list) #import using arr

a=array(data type,value list) #import using * (from array import *)
 
'''

import numpy
import array
usia = array.array('i', [19, 12, 13, 14, 12, 11, 20, 22])


print(usia[0])

try:
    usia[0] = 10
except:
    print("value array usia harus bertipe integer")

print(usia[0])
print(hex(id(usia)))


# menggunakan numpy
np_array = numpy.array([1, 2, 3, 4, 5])
print(np_array)
