# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans: List[List[str]] = []
        part: List[str] = []

        def dfs(start: int):
            if start == len(s):
                ans.append(list(part))  # copy current path because it is shared
                return

            for i in range(start + 1, len(s) + 1):
                sub = s[start:i]

                if self._palindrome(sub):
                    part.append(sub)
                    dfs(i)
                    part.pop()  # backtrack

        dfs(0)
        return ans

    def _palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        return left >= right


assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
assert Solution().partition("banana") == [
    ["b", "a", "n", "a", "n", "a"],
    ["b", "a", "n", "ana"],
    ["b", "a", "nan", "a"],
    ["b", "ana", "n", "a"],
    ["b", "anana"],
]
