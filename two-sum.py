# https://leetcode.com/problems/two-sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_and_index = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            
            if diff in value_and_index:
                return [value_and_index[diff], i]
            
            value_and_index[v] = i
        
        raise "No solution"

# Tests

assert Solution().twoSum(nums = [2,7,11,15], target = 9) ==  [0,1]
assert Solution().twoSum(nums = [3,2,4], target = 6) == [1,2]
assert Solution().twoSum(nums = [3,3], target = 6) == [0,1]
