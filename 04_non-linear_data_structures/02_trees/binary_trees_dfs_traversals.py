class TreeNode:
    """A node in a binary tree with at most one left and one right child."""

    def __init__(self, value):
        self.value = value
        # Neue Knoten starten ohne Kinder; diese werden beim Einfügen verknüpft.
        self.left = None
        self.right = None


class BinaryTree:
    """A binary tree that keeps a reference to its root node."""

    def __init__(self, root_value):
        # Der Wurzelknoten ist der Einstiegspunkt für alle weiteren Operationen.
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, new_value):
        # If a left child already exists, preserve it below the new node.
        new_node = TreeNode(new_value)
        if current_node.left is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        # If a right child already exists, preserve it below the new node.
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node


# Build the example tree:
#          R
#        /   \
#       A     B
#      / \   / \
#     C   D E   F

# 1) Create a tree with root 'R'.
bt = BinaryTree("R")

# 2) Insert 'A' as left child of 'R', and 'B' as right child of 'R'.
bt.insert_left(bt.root, "A")  # nodeA
bt.insert_right(bt.root, "B")  # nodeB

# 3) Get references to the newly inserted nodes for further insertions.
nodeA = bt.root.left
nodeB = bt.root.right

# 4) Insert 'C' and 'D' under 'A'.
bt.insert_left(nodeA, "C")
bt.insert_right(nodeA, "D")

# 5) Insert 'E' and 'F' under 'B'.
bt.insert_left(nodeB, "E")
bt.insert_right(nodeB, "F")

# Test: Zugriff auf den Knoten 'E' (bt.root.right.left).
print("root.right.left.value:", bt.root.right.left.value)  # Should print 'E'


def pre_order(node, visited):
    # Ein leerer Teilbaum beendet diesen rekursiven Pfad.
    if node is None:
        return

    # Pre-Order: Knoten, linker Teilbaum, rechter Teilbaum.
    visited.append(node.value)
    pre_order(node.left, visited)
    pre_order(node.right, visited)


# Die Liste sammelt die Besuchsreihenfolge, ohne den Baum zu verändern.
pre_order_values = []
pre_order(bt.root, pre_order_values)
print(pre_order_values)


def in_order(node, visited):
    # Auch hier beendet ein leerer Teilbaum den rekursiven Aufruf.
    if node is None:
        return

    # In-Order: linker Teilbaum, Knoten, rechter Teilbaum.
    in_order(node.left, visited)
    visited.append(node.value)
    in_order(node.right, visited)


# Bei einem binären Suchbaum würde diese Reihenfolge die Werte sortiert liefern.
in_order_values = []
in_order(bt.root, in_order_values)
print(in_order_values)


def post_order(node, visited):
    # Ein leerer Teilbaum enthält keinen Knoten, der besucht werden könnte.
    if node is None:
        return

    # Post-Order: linker Teilbaum, rechter Teilbaum, Knoten.
    post_order(node.left, visited)
    post_order(node.right, visited)
    visited.append(node.value)


# Der Knoten wird erst eingetragen, nachdem beide Teilbäume bearbeitet wurden.
post_order_values = []
post_order(bt.root, post_order_values)
print(post_order_values)
