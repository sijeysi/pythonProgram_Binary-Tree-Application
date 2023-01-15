# Binary Tree Part 1 Exercise

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
    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # Val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data: 
            # Val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    # in_order_traversal(): performs in order traversal of a binary tree
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    # pre_order_traversal(): performs pre order traversal of a binary tree
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
        
