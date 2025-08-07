class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    
class binarySearchTree():
    def __init__(self):
        self.root = None 

    def _is_empty(self):
        return self.root is None
    
    def insert(self, data):
        
        if self._is_empty():
            self.root = Node(data)
            
            
        else:
            self._insertRecursive(self.root, data)
            
    def _insertRecursive(self, current,data):
        if data < current.value:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insertRecursive(current.left,data)
        elif data >= current.value:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insertRecursive(current.right,data)
    
    def search(self, query):
        return self._search_recursive(self.root,query=query)
            
    def _search_recursive(self,current: Node ,query: str):
        if not current:
            return "FALSE"
        elif current.value == query:
            return "TRUE"
        elif query >= current.value:
            self._search_recursive(current.right,query)
        elif query < current.value:
            self._search_recursive(current.left,query)
            
            
tree = binarySearchTree()
tree.insert(5)
print("sudah masuk 5")
tree.insert(3)
tree.insert(10)
tree.insert(7)
print(tree.search(5))