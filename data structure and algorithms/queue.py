'''
queue : FIFO – First In, First Out
Elemen yang masuk lebih dulu, akan keluar lebih dulu juga.

analogi = antrian

'''

from collections import deque

class queue:
    def __init__(self):
        self.items = deque()
        
    def enqueu(self, item):
        try:
            self.items.append(item)
            print(f"{item} sukses ditambahkan")
        except:
            print("data gagal ditambahkan")
    
    def dequeue(self):
        if self.items:
            return self.items.popleft()
        return "list kosong"
    
    def peek(self):
        if self._is_empty:
            return self.items[0]
        return "list kosong"
    
    def _is_empty(self):
        return not bool(self.items)
    
antrian = queue()
print(antrian._is_empty())
antrian.enqueu(1)
antrian.enqueu(2)
antrian.enqueu(3)
antrian.enqueu(4)
print(f"antrian sekarang = {antrian.peek()}")
print(antrian.dequeue())
print(f"antrian sekarang = {antrian.peek()}")
print(antrian._is_empty())