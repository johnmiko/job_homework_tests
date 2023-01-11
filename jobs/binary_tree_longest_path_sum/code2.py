class BinaryTreeNode:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.leftNode = None
        self.rightNode = None


def SumOfLongRootToLeafPath(root, cumulative, len, maxLen, maxSum):
    if not root:
        if maxLen[0] < len:
            maxLen[0] = len
            maxSum[0] = cumulative
        elif (maxLen[0] == len and
              maxSum[0] < cumulative):
            maxSum[0] = cumulative
        return

    # recur for left subtree
    SumOfLongRootToLeafPath(root.leftNode, cumulative + root.nodeValue,
                            len + 1, maxLen, maxSum)

    # recur for right subtree
    SumOfLongRootToLeafPath(root.rightNode, cumulative + root.nodeValue,
                            len + 1, maxLen, maxSum)


def longestBranch(root):
    if not root:
        return 0

    maxSum = [-999999999999]
    maxLen = [0]
    SumOfLongRootToLeafPath(root, 0, 0, maxLen, maxSum)
    return maxSum[0]


# Driver Code
if __name__ == '__main__':
    # binary tree formation
    root = BinaryTreeNode(4)  # 4
    root.left = BinaryTreeNode(2)  # / \
    root.rightNode = BinaryTreeNode(5)  # 2 5
    root.left.left = BinaryTreeNode(7)  # / \ / \
    root.left.rightNode = BinaryTreeNode(1)  # 7 1 2 3
    root.rightNode.left = BinaryTreeNode(2)  # /
    root.rightNode.rightNode = BinaryTreeNode(3)  # 6
    root.left.rightNode.left = BinaryTreeNode(6)

    print("Sum = ", longestBranch(root))

# This code is contributed by PranchalK
