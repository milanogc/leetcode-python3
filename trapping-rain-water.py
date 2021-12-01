# https://leetcode.com/problems/trapping-rain-water

from typing import List

class Solution:
    def trapWithoutMinMax(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        highest_height = 0
        trapped_water = 0

        while left < right:
            if height[right] > height[left]:
                if highest_height < height[left]:
                    highest_height = height[left]
                trapped_water += highest_height - height[left]
                left += 1
            else:
                if highest_height < height[right]:
                    highest_height = height[right]
                trapped_water += highest_height - height[right]
                right -= 1
        
        return trapped_water

    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        highest_height = 0
        trapped_water = 0
        
        while left < right:
            current_height = min(height[right], height[left])
            highest_height = max(highest_height, current_height)
            trapped_water += highest_height - current_height

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return trapped_water

# Tests

# Solution.trap = Solution.trapWithoutMinMax

assert Solution().trap([]) == 0
assert Solution().trap([1]) == 0
assert Solution().trap([0,0]) == 0
assert Solution().trap([0,1]) == 0
assert Solution().trap([1,0]) == 0
assert Solution().trap([1,1]) == 0
assert Solution().trap([0,0,0]) == 0
assert Solution().trap([0,0,1]) == 0
assert Solution().trap([1,0,1]) == 1
assert Solution().trap([1,1,0]) == 0
assert Solution().trap([1,1,1]) == 0
assert Solution().trap([0,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0]) == 26
