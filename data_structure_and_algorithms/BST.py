'''
bst = node(value, left, right)

inorder = sort small -> high
preorder = print jalan yang dilalui saat mencari node paling kecil sampai semua node di print
postorder = print dari node terakhir paling kiri


'''

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
    
    def _inorder_traversal(self,current: Node):
        if current.left:
            self._inorder_traversal(current.left)
        print(current.value)
        if current.right:
            self._inorder_traversal(current.right)
            
    
    def _preorder_traversal(self,current: Node):
        print(current.value)
        if current.left:
            self._preorder_traversal(current.left)
        if current.right:
            self._preorder_traversal(current.right)
        
    
    def _postorder_traversal(self,current: Node):
        if current.left:
            self._postorder_traversal(current.left)
        if current.right:
            self._postorder_traversal(current.right)
        print(current.value)
    
    def delete(self, current : Node, data):
        if data < current.value:
            current.left = self.delete(current.left, data)
        elif data > current.value:
            current.right = self.delete(current.right, data)
        else:
            if data == current.value:
                if current.left is None and current.right is None:
                    current = None
                    return current
                elif current.left and current.right is None:
                    current = current.left
                    return current
                elif current.right and current.left is None:
                    current = current.right
                    return current
                
                elif current.left and current.right:
                    current.value = self._inorder_successor(current=current.right)
                    current.right = self.delete(current.right, current.value)
        return current
                
    def _inorder_successor(self, current: Node):
        if current.left is None:
            return current.value
        return self._inorder_successor(current.left)
        
            
tree = binarySearchTree()
tree.insert(5)
# print("sudah masuk 5")
tree.insert(3)
tree.insert(3)
tree.insert(10)
tree.insert(7)
print(tree.search(5))
# tree._inorder_traversal(current=tree.root)
# tree._preorder_traversal(current=tree.root)
tree._postorder_traversal(current=tree.root)
