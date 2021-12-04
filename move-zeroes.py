# https://leetcode.com/problems/move-zeroes

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        write_index = read_index = 0

        while read_index < length:
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1
            
            read_index += 1
        
        while write_index < length:
            nums[write_index] = 0
            write_index += 1

# Tests

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
assert nums == [1,3,12,0,0]
nums = [0]
Solution().moveZeroes(nums)
assert nums == [0]
