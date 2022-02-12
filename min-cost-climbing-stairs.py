# https://leetcode.com/problems/min-cost-climbing-stairs

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        for i in range(2, n):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[n - 1], cost[n - 2])


# Tests

Solution().minCostClimbingStairs([10, 15, 20]) == 15
Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
