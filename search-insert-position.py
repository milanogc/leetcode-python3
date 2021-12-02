# https://leetcode.com/problems/search-insert-position

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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

        return start

# Tests

assert Solution().searchInsert(nums = [1,3,5,6], target = 5) == 2
assert Solution().searchInsert(nums = [1,3,5,6], target = 2) == 1
assert Solution().searchInsert(nums = [1,3,5,6], target = 7) == 4
assert Solution().searchInsert(nums = [1,3,5,6], target = 0) == 0
assert Solution().searchInsert(nums = [1], target = 0) == 0
assert Solution().searchInsert(nums = [1], target = 1) == 0
assert Solution().searchInsert(nums = [1], target = 2) == 1
assert Solution().searchInsert(nums = [1,2], target = 3) == 2
assert Solution().searchInsert(nums = [1,3], target = 3) == 1