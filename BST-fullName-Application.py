# Using the letters of my full name as the content of the binary tree.

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
    
    # post_order_traversal(): performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    # find_min(): finds minimum element in entire binary tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    # find_max(): finds maximum element in entire binary tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    # delete(): delete element
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


# Build Binary Tree
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root 

if __name__ == '__main__':
    numbers = ["C", "R", "Y", "S", "T", "A", "L", 
                "J", "A", "N", "E",
                "C", "A", "D", "I", "M", "A", "S"]
    lettersName = build_tree(numbers)

    print("Full Name: CRYSTAL JANE CADIMAS", "\n")
    print("Minimum letter:", lettersName.find_min())
    print("Maximum letter:", lettersName.find_max(), "\n")

    print("In order traversal:", lettersName.in_order_traversal())
    print("Pre order traversal:", lettersName.pre_order_traversal())
    print("Post order traversal:", lettersName.post_order_traversal(), "\n")

    print("Letter 'A' is in the list?", lettersName.search("A"))
    print("Letter 'Z' is in the list?", lettersName.search("Z"), "\n")

    lettersName.delete("A")
    print("After deleting 'A':", lettersName.in_order_traversal())
    print("Updated minimum letter:", lettersName.find_min())
    print("Updated maximum letter:", lettersName.find_max())
    