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

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root 

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9 , 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())    
    print(numbers_tree.search(200))

    print("\n")
    
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print("UK is in the list?", country_tree.search("UK"))
    print("Sweden is in the list?", country_tree.search("Sweden"))

    print(country_tree.in_order_traversal())
    