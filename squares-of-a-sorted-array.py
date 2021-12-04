# https://leetcode.com/problems/squares-of-a-sorted-array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        right = length - 1
        left = 0
        ans = [0] * length

        for index in range(right, -1, -1):
            left_sq = nums[left]**2
            right_sq = nums[right]**2

            if right_sq > left_sq:
                ans[index] = right_sq
                right -= 1
            else:
                ans[index] = left_sq
                left += 1
        
        return ans

# Tests

assert Solution().sortedSquares(nums = [-4,-1,0,3,10]) == [0,1,9,16,100]
assert Solution().sortedSquares(nums = [-7,-3,2,3,11]) == [4,9,9,49,121]
assert Solution().sortedSquares(nums = [-5,-4,-3,-2,-1]) == [1,4,9,16,25]
assert Solution().sortedSquares(nums = [1,2,3,4,5]) == [1,4,9,16,25]
