# https://leetcode.com/problems/rotate-array

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        self._reverse(nums, 0, length - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, length - 1)
    
    def _reverse(self , nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Tests

nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
assert nums == [5,6,7,1,2,3,4]
nums = [-1,-100,3,99]
Solution().rotate(nums, 2)
assert nums == [3,99,-1,-100]
nums = [-1]
Solution().rotate(nums, 2)
assert nums == [-1]
