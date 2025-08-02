class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def show_all(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("done")

    def add_last(self, paramData: str):
        newNode = Node(paramData)

        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode

    def add_front(self, paramData: str):
        newNode = Node(paramData)
        newNode.next = self.head
        self.head = newNode

    def delete(self, paramData):
        current = self.head
        prev = None

        while current:
            if current.data == paramData:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
                current = current.next

    def addBetween(self, paramData, query):
        newNode = Node(paramData)
        current = self.head
        prev = None
        while current:
            if current.data == query:
                if prev is None:
                    newNode.next = self.head
                    self.head = newNode
                else:
                    prev.next = newNode
                    newNode.next = current
                return
            else:
                prev = current
                current = current.next

    def search(self, query):
        current = self.head
        while current:
            if current.data == query:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


antrian = linkedList()

antrian.add_front("juana")


antrian.add_last("made")
antrian.add_last("komang")

antrian.show_all()
print(antrian.search("aku"))

antrian.addBetween("halimawan", "komang")
antrian.show_all()

print(f"panjang antrian adalah : {antrian.length()}")
