# https://leetcode.com/problems/average-of-levels-in-binary-tree

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        nums_sum = 0
        nums_count = nums_remaining = 1
        ans = []

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            nums_sum += node.val
            nums_remaining -= 1

            if not nums_remaining:
                ans.append(nums_sum / nums_count)
                nums_sum = 0
                nums_count = nums_remaining = len(queue)

        return ans


# Tests

T = TreeNode

# fmt: off

assert Solution().averageOfLevels(None) == []
assert Solution().averageOfLevels(T(3, T(9), T(20, T(15), T(7)))) == [3.00000,14.50000,11.00000]
assert Solution().averageOfLevels(T(3, T(9, T(15), T(7)), T(20))) == [3.00000,14.50000,11.00000]
assert Solution().averageOfLevels(T(4, T(7, T(10), T(2, None, T(6, T(2)))), T(9, None, T(6)))) == [4, 8, 6, 6, 2,]

# fmt: on
