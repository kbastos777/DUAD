class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert_left(self, current_node, data):
        
        if current_node.left is None:
            current_node.left = Node(data)
        else:
            print(f"El nodo con valor {current_node.data} ya tiene un hijo izquierdo.")

    def insert_right(self, current_node, data):
        
        if current_node.right is None:
            current_node.right = Node(data)
        else:
            print(f"El nodo con valor {current_node.data} ya tiene un hijo derecho.")

    def print_structure(self, node=None, level=0):
        
        if node is None:
            node = self.root

        if node.right:
            self.print_structure(node.right, level + 1)

        print("    " * level + f"-> {node.data}")

        if node.left:
            self.print_structure(node.left, level + 1)



binary_tree = BinaryTree("A")


binary_tree.insert_left(binary_tree.root, "B") 
binary_tree.insert_right(binary_tree.root, "C")  

binary_tree.insert_left(binary_tree.root.left, "D") 
binary_tree.insert_right(binary_tree.root.left, "E")  

binary_tree.insert_left(binary_tree.root.right, "F")  
binary_tree.insert_right(binary_tree.root.right, "G") 


print("Estructura del Binary Tree con letras:")
binary_tree.print_structure()
