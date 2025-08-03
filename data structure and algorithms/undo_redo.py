class state:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class undo_redo_manager:
    def __init__(self):
        self.head = None
        self.current = None
        
    def tambah_state(self, data: str):
        new_node = state(data)
        if self.head is None:
            self.head = new_node
            self.current = new_node
        else:
            if self.current.next:
                self.current.next.prev = None
                self.current.next = None
            
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node
    
    def undo(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        else:
            return "tidak bisa undo"
        
    def redo(self):
        if self.current.next and self.current:
            self.current = self.current.next
            return self.current.data
        else:
            return "tidak bisa redo"
        
    def currentState(self):
        current = self.head
        count = 1
        while current:
            if current.data == self.current.data:
                print(f"kamu ada di state no : {count}")
                return self.current.data
            count+=1
            current = current.next
                
        

chat = undo_redo_manager()
chat.tambah_state("halooo...")
chat.tambah_state("nama saya juana")
chat.tambah_state("nama saya ")
chat.tambah_state("nama saya juana satya adinata")



chat.currentState()
chat.undo()
chat.undo()
print(chat.undo())
chat.currentState()
print(chat.undo())