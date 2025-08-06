'''
Heaps Stacks and Queues

| Struktur Data | Prinsip Utama             | Operasi Umum          | Contoh Kegunaan                   |
| ------------- | ------------------------- | --------------------- | --------------------------------- |
| **Stack**     | LIFO (Last In First Out)  | `push`, `pop`, `peek` | Undo di editor, parsing (rekursi) |
| **Queue**     | FIFO (First In First Out) | `enqueue`, `dequeue`  | Antrian tiket, proses printer     |
| **Heap**      | Priority (min/max)        | `insert`, `extract`   | Priority queue, scheduling        |


'''

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return "Stack kosong"
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return "list kosong"
    
    def display(self):
        print(f"list dari urutan paling kanan adalah atas = {self.items}")
             
             
rak = Stack()
rak.push(10)
rak.push(20)
rak.push(30)
rak.display()
print(rak.peek())