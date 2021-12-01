# https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        status = 0
        left_pos = None
        right_pos = None

        while left < right:
            if s[left] != s[right]:
                if status == 0: # no char was removed til now... try removing from left
                    left_pos = left
                    right_pos = right
                    left += 1
                    status = 1
                elif status == 1: # char was removed from left... try removing from right
                    left = left_pos
                    right = right_pos - 1
                    status = 2
                else: # chars removed from left and right already...
                    return False
            else:
                left += 1
                right -= 1
        
        return  True

# Tests

assert Solution().validPalindrome("raceacar") == True
assert Solution().validPalindrome("abccdba") == True
assert Solution().validPalindrome("abcdefdba") == False
assert Solution().validPalindrome("") == True
assert Solution().validPalindrome("a") == True
assert Solution().validPalindrome("ab") == True
assert Solution().validPalindrome("abc") == False
assert Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True
assert Solution().validPalindrome("abbab") == True
