# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for p in prices[1:]:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)

        return max_profit

# Tests

assert Solution().maxProfit([]) == 0
assert Solution().maxProfit([1]) == 0
assert Solution().maxProfit([1,2]) == 1
assert Solution().maxProfit([2,1]) == 0
assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0
assert Solution().maxProfit([6,1,3,2,4,7]) == 6
