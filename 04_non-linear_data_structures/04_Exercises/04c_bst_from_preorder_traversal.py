# Variante 1 von Kevin
# Aufgabe 1: BST from preorder traversal

# Rekonstruiere aus `preorder` einen binären Suchbaum und gib dessen Wurzel zurück. Links stehen strikt kleinere, rechts strikt größere Werte. Preorder besucht Wurzel, linken und rechten Teilbaum. Alle Werte sind eindeutig; ein gültiger Baum ist garantiert.

# Beispiel: `[8,5,1,7,10,12]` → Level-Reihenfolge `[8,5,10,1,7,None,12]`; `[1,3]` → `[1,None,3]`.

# Meine Lösung:


keys = [8, 5, 1, 7, 10, 12]
printlist = []


class Node:
    def __init__(self, key):
        self.key = key
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, key):
        self.root = self.recursive_insert(self.root, key)

    def recursive_insert(self, node: Node, key):
        if node is None:
            # trifft auch auf root zu.
            return Node(key)
        if key < node.key:
            node.left = self.recursive_insert(node.left, key)
        if key > node.key:
            node.right = self.recursive_insert(node.right, key)
        return node

    def print_tree(self, print_list: list):
        self.print_tree_recursive(self.root, print_list)

    def print_tree_recursive(self, node: Node, print_list: list):
        if node is None:
            return
        elif (node.left is None and node.right is not None) or (
            node.left is not None and node.right is None
        ):
            print_list.append("null")
        print_list.append(node.key)
        self.print_tree_recursive(node.left, print_list)
        self.print_tree_recursive(node.right, print_list)


bst = BinarySearchTree()
for key in keys:
    bst.add_node(key)
bst.print_tree(printlist)
print(printlist)
# print(bst.print_tree([]))
