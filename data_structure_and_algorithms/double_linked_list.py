class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
    
    def show_forward(self):
        current = self.head
            
        while current:
            print(current.data,end=' ⇄ ')
            current = current.next
        print("none")
        
    def show_backward(self):
        current = self.head
        
        while current.next: #cek setelah node ini ada node lagi atau tidak
            current = current.next
        
        while current: # cek node sekarang ada data atau tidak jika ada lanjut
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")
            
    def add_back(self,query):
        new_node = Node(query)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next :
                current = current.next
            current.next = new_node
            new_node.prev = current
            
    def add_front(self,query):
        new_node = Node(query)
        current = self.head
        if current is None:
            self.head = new_node
            return
        else:
            current.prev = new_node
            new_node.next = current
            self.head = new_node
            
    def delete(self,query):
        current = self.head
        
        while current:
            if current.data == query:
                if current == self.head:
                    self.head = current.next
                    return
                else:
                    current.prev.next = current.next 
                    if current.next:
                        current.next.prev = current.prev  
                    return
            else:
                current = current.next
                
                    
        
dll = doubleLinkedList()
dll.add_back(10)
dll.add_back(50)
dll.add_front(100)
dll.show_forward()
dll.show_backward()

dll.delete(10)
dll.show_backward()