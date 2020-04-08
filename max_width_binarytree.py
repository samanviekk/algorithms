import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def widthOfBinaryTree(root: TreeNode) -> int:
    if root is None:
        return 0

    maxwidth = 1
    q = collections.deque([(root, 1)])
    while len(q) != 0:
        numnodes = len(q)

        leftmost = float("inf")
        rightmost = float("-inf")
        for _ in range(numnodes):

            (node, id) = q.popleft()
            if leftmost == float("inf"):
                leftmost = id
            rightmost = max(rightmost, id)

            if node.left is not None:
                q.append((node.left, 2 * id))
            if node.right is not None:
                q.append((node.right, 2 * id + 1))

        levelwidth = rightmost - leftmost + 1
        if levelwidth > maxwidth:
            maxwidth = levelwidth

    return maxwidth

def widthOfBinaryTree1(root: TreeNode) -> int:
    if root is None:
        return 0

    maxwidth = 1
    q = collections.deque([(root, 1)])
    while len(q) != 0:
        numnodes = len(q)

        first = None
        last = None
        for _ in range(numnodes):
            (node, id) = q.popleft()

            if node.left is not None:
                q.append((node.left, 2 * id))
            if node.right is not None:
                q.append((node.right, 2 * id + 1))

            last = id
            if first is None:
                first = id
        maxwidth = max(maxwidth, last-first+1)

    return maxwidth

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

input = [1, 3, 2, 5, 3, 'null', 9]
root = build_tree(input)
print(widthOfBinaryTree1(root))
