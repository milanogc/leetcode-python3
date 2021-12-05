# https://leetcode.com/problems/reverse-string

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

s = ["h","e","l","l","o"]
Solution().reverseString(s)
assert s == ["o","l","l","e","h"]
s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
assert s == ["h","a","n","n","a","H"]
