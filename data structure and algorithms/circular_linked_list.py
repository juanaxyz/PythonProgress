class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class circular_linked_list:
    def __init__(self):
        self.head = None
    
    def add_back(self,query: str):
        new_node = Node(query)
        current = self.head
        if not current:
            self.head = new_node
            new_node.next = self.head
        else:
            while current.next != self.head :
                current = current.next
            current.next = new_node
            new_node.next = self.head 
            
    def add_front(self, data: str):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            new_node.next = self.head
            return
        while current.next != self.head:
            current = current.next
        
        current.next = new_node
        new_node.next = self.head
        self.head = new_node
    
    def delete(self,query):
        if self.head is None:
            print("list kosong")
            return
        
        current = self.head
        # jika head == query
        if current.data == query:
            # cek apakah next node = head
            if current.next == self.head:
                self.head = None
                return
            else:
                tail = self.head #cari node ekor/tail
                while tail.next !=  self.head:
                    tail = tail.next
                # update node ekor ke setelah current
                self.head = current.next
                tail.next = current.next
            return
        
        # jika tidak ada di node pertama
        
            
        prev = current
        current = current.next
        while current != self.head:
            if current.data == query:
                prev.next = current.next
                return
            prev = current
            current = current.next
        
        print(f"data '{query}' tidak ditemukan")

            

    def show(self):
        if not self.head:
            print( "list kosong")
            return
        else:
            current = self.head
            while current:
                if current.next == self.head:
                    break
                print(current.data,end=" -> ")
                current = current.next
            print("kembali ke awal/head")
                
cll = circular_linked_list()
cll.add_back("A")
cll.add_back("B")
cll.add_back("C")
cll.add_back("D")
cll.show()

# Output:
# A → B → C → (kembali ke awal)
