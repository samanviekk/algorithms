import collections
class TreeNode:
    def __init__(self, x):
        self. val = x
        self.left = None
        self.right = None

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
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        result.append(temp)
    return result

def level_order_recursive(root):
    if root is None:
        return []
    result = []
    def helper(q):
        if len(q) == 0:
            return
        temp = []
        newq = []
        for node in q:
            temp.append(node.val)
            if node.left is not None:
                newq.append(node.left)
            if node.right is not None:
                newq.append(node.right)
        result.append(temp[:])
        helper(newq)
    helper([root])
    return result




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

input = [3, 9, 20, 15, 17, 8, 'null']
root = build_tree(input)
res = level_order_traversal(root)
print(res)
result = level_order_recursive(root)
print("recursive:", result)






