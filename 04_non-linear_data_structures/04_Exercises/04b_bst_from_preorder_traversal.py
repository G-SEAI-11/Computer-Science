# LMS Musterlösung
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(preorder):
    def helper(lower=float("-inf"), upper=float("inf")):
        nonlocal idx
        # If all elements from preorder are used
        # Then the tree is constructed
        if idx == n:
            return None

        val = preorder[idx]
        # If the current element
        # couldn't be placed here to meet BST requirements
        if val < lower or val > upper:
            return None

        # place the current element
        # and recursively construct subtrees
        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root

    idx = 0
    n = len(preorder)
    return helper()


# To visualize the Tree as a list
def tree_to_list_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


root = bstFromPreorder([8, 5, 1, 7, 10, 12])
print(tree_to_list_level_order(root))
