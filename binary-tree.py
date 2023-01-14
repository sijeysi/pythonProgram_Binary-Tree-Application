class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # Add data in left subtree
            if self.left:
                self.left.add_child(data)
            else: 
                self.left = BinarySearchTreeNode(data)
        else: 
            # Add data in right subtree
            if self.right:
                self.right.add_child(data)
            else: 
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)

        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
        