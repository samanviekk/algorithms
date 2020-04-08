import collections
class TreeNode:
    def __init__(self, x):
        self. val = x
        self.left = None
        self.right = None

def is_symmetric(root):
    def check_symmetric(subtree_0, subtree_1):
        if subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.val == subtree_1.val
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        return False
    return not root or check_symmetric(root.left, root.right)



def build_tree(input):
    def helper(input, i):
        if i >= len(input):
            return None
        if input[i] == 'null':
            return None
        node = TreeNode(input[i])
        node.left = helper(input, 2 * i + 1)
        node.right = helper(input, 2 * i + 2)
        return node

    node = helper(input, 0)
    return node

input = [1, 2, 2, 3, 4, 4, 3]
root = build_tree(input)
print(is_symmetric(root))