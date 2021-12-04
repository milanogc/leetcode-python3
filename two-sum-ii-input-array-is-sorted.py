# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            two_sum = nums[left] + nums[right]
    
            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        raise "No solution"

# Tests

assert Solution().twoSum(nums = [2,7,11,15], target = 9) == [1,2]
assert Solution().twoSum(nums = [2,3,4], target = 6) == [1,3]
assert Solution().twoSum(nums = [-1,0], target = -1) == [1,2]
