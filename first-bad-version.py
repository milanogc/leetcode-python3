# https://leetcode.com/problems/first-bad-version

bad = None

def isBadVersion(n: int) -> bool:
    return n >= bad

class Solution:
    def firstBadVersion(self, n: int) -> bool:
        start = 1
        end = n
        bad_version = n
        
        while start <= end:
            middle = (start + end) // 2
            
            if isBadVersion(middle):
                bad_version = middle
                end = middle - 1
            else:
                start = middle + 1
        
        return bad_version

bad = 4
assert Solution().firstBadVersion(5) == bad
bad = 1
assert Solution().firstBadVersion(1) == bad
