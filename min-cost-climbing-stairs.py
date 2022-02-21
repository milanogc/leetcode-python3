# https://leetcode.com/problems/min-cost-climbing-stairs

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1 = cost[0]
        c2 = cost[1]

        for i in range(2, len(cost)):
            c1, c2 = c2, cost[i] + min(c1, c2)

        return min(c1, c2)


# Tests

Solution().minCostClimbingStairs([10, 15, 20]) == 15
Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
