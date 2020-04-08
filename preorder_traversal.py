class TreeNode:
    def __init__(self, x):
        self. val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        self.preorder_traversal_helper(root, res)
        return res

    def preorder_traversal_helper(self, root, res):
        if root == None: return
        res.append(root.val)
        self.preorder_traversal_helper(root.left, res)
        self.preorder_traversal_helper(root.right, res)

    def preorder_iter(self, root):
        res = []
        if root == None: return res
        stack = []
        stack.append(root)
        while len(stack) != 0:
            n = stack.pop()
            res.append((n.val))
            if n.right is not None:
                stack.append(n.right)
            if n.left is not None:
                stack.append(n.left)
        return res



root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print(s.preorderTraversal(root))
print(s.preorder_iter(root))