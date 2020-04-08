class TreeNode:
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

import collections
def clone_tree(root):
    if root is None:
        return None

    root2 = TreeNode(root.val)
    q = collections.deque([(root, root2)])
    while len(q) != 0:
        numnodes = len(q)
        for _ in range(numnodes):
            node, node2 = q.popleft()
            if node.left_ptr is not None:
                node2.left_ptr = TreeNode(node.left_ptr.val)
                q.append((node.left_ptr, node2.left_ptr))
            if node.right_ptr is not None:
                node2.right_ptr = TreeNode(node.right_ptr.val)
                q.append((node.right_ptr, node2.right_ptr))
    return root2

def build_tree(input):
    def helper(input, i):
        if i >= len(input):
            return None
        if input[i] == 'null':
            return None
        node = TreeNode(input[i])
        node.left_ptr = helper(input, 2 * i + 1)
        node.right_ptr = helper(input, 2 * i + 2)
        return node

    node = helper(input, 0)
    return node

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    q = collections.deque([root])
    while len(q) != 0:
        numnodes = len(q)
        temp = []
        for _ in range(numnodes):
            node = q.popleft()
            temp.append(node.val)
            if node.left_ptr is not None:
                q.append(node.left_ptr)
            if node.right_ptr is not None:
                q.append(node.right_ptr)
        result.append(temp)
    return result

input = [3, 9, 20, 15, 17, 8, 'null']
root = build_tree(input)
print(level_order_traversal(root))
root2 = clone_tree(root)
print(level_order_traversal(root))
res = level_order_traversal(root2)
print(res)



