class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        while current:
            # print(current)
            print(current.data, end=" -> ")
            current = current.next

        print("none")

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


ll = linkedList()
ll.add_last(10)
ll.add_front(5)

ll.show()

ll2 = linkedList()
ll2.show()

ll.reverse()
ll.show()
