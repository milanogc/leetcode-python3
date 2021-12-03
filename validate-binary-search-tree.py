# https://leetcode.com/problems/validate-binary-search-tree

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, left: int = -math.inf, right: int = math.inf) -> bool:
        return not root or (
            left < root.val < right and
            self.isValidBST(root.left, left, root.val) and
            self.isValidBST(root.right, root.val, right)
        )

# Tests

from typing import List

# https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-

def createBinaryTree(data: List[int], index = 0) -> TreeNode:
    node = None

    if index < len(data):
        if data[index] == None:
            return None

        node = TreeNode(data[index])
        node.left = createBinaryTree(data, 2 * index + 1)
        node.right = createBinaryTree(data, 2 * index + 2)

    return node 

assert Solution().isValidBST(root = createBinaryTree([2,1,3]))
assert Solution().isValidBST(root = createBinaryTree([5,1,4,None,None,3,6])) == False
