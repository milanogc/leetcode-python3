# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        n = len(s)
        max_length = 0

        for left in range(n):
            seen_chars = set()
            
            for right in range(left, n):
                if s[right] in seen_chars:
                    break

                seen_chars.add(s[right])
            
            max_length = max(max_length, len(seen_chars))
        
        return max_length
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, c in enumerate(s):
            if c in char_index and left <= char_index[c]:
                left = char_index[c] + 1

            char_index[c] = right
            max_length = max(max_length, right - left + 1)

        return max_length

# Tests

# Solution.lengthOfLongestSubstring = Solution.lengthOfLongestSubstringBruteForce

assert Solution().lengthOfLongestSubstring("abba") == 2
assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring("a") == 1
assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5
assert Solution().lengthOfLongestSubstring("dvdf") == 3
