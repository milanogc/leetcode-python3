# https://leetcode.com/problems/binary-search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                return middle
        
        return -1

assert Solution().search(nums = [-1,0,3,5,9,12], target = 9) == 4
assert Solution().search(nums = [-1,0,3,5,9,12], target = 2) == -1