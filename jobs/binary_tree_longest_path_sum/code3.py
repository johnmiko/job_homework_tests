class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create dataclass to store current node, and sum of values up to this point
class NodeSum:
    def __init__(self, node, sum):
        self.node = node
        self.sum = sum


def longestBranch(root):
    level = 0
    items = [[NodeSum(root, root.value)]]

    while True:
        cur_row = []
        for item in items[level]:
            if item.node.left is not None:
                cur_row.append(NodeSum(item.node.left, item.node.left.value + item.sum))
            if item.node.right is not None:
                cur_row.append(NodeSum(item.node.right, item.node.right.value + item.sum))
        if not cur_row:
            break
        items.append(cur_row)
        level += 1
    max_value = 0
    for item in items[-1]:
        if item.sum > max_value:
            max_value = item.sum
    return max_value


root = BinaryTreeNode(4)  # 4
root.left = BinaryTreeNode(2)  # / \
root.right = BinaryTreeNode(5)  # 2 5
root.left.left = BinaryTreeNode(7)  # / \ / \
root.left.right = BinaryTreeNode(1)  # 7 1 2 3
root.right.left = BinaryTreeNode(2)  # /
root.right.right = BinaryTreeNode(3)  # 6
root.left.right.left = BinaryTreeNode(6)
