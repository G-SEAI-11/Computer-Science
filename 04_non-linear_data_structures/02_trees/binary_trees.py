# class BinaryNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# root = BinaryNode("R")
# root.left = BinaryNode("A")
# root.right = BinaryNode("B")
# root.left.left = BinaryNode("C")
# root.left.right = BinaryNode("D")
# root.right.left = BinaryNode("E")
# root.right.right = BinaryNode("F")


class TreeNode:
    """A node in a binary tree with at most one left and one right child."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """A binary tree that keeps a reference to its root node."""

    def __init__(self, root_value):
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

# Test: Access node 'E' (which is bt.root.right.left)
print("root.right.left.value:", bt.root.right.left.value)  # Should print 'E'
