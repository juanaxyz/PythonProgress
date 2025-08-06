import heapq

class antrianPrior:
    def __init__(self):
        self.queue = []
        self.counter = 0
        
    def _is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self,priority: int,name: str):
        heapq.heappush(self.queue,(priority,self.counter, name))
        # print(len(self.queue))
        self.counter +=1
    
    def dequeue(self):
        if not self._is_empty():
            return heapq.heappop(self.queue)
        return "antrian kosong"
    
    def peek(self):
        if not self._is_empty():
            return self.queue[0][2]
        return "list kosong"
    
    def display(self):
        print("Semua Antrian :")
        for item in sorted(self.queue):
            print(f"\t - {item[2]}")
        
        
    

antrianUGD = antrianPrior()

# print(antrianUGD.peek())
antrianUGD.enqueue(1, "juana")
antrianUGD.enqueue(2, "made")
antrianUGD.enqueue(2, "made2")
antrianUGD.enqueue(1, "madek")
# print(antrianUGD.peek())
# antrianUGD.display()
print(f"saat ini : {antrianUGD.peek()}")
antrianUGD.display()
# antrianUGD.dequeue()
print(f"selesai : {antrianUGD.dequeue()[2]}")
antrianUGD.display()