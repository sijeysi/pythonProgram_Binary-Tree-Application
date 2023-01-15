from BinarySearchTree import BinarySearchTreeNode

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root 

if __name__ == '__main__':
    letters = ["C", "R", "Y", "S", "T", "A", "L", 
                "J", "A", "N", "E",
                "C", "A", "D", "I", "M", "A", "S"]
    lettersName = build_tree(letters)

    print("Full Name: CRYSTAL JANE CADIMAS")
    