# https://leetcode.com/problems/backspace-string-compare

import itertools

class Solution:
    def _removeBackspacesBruteForce(self, s: str):
        stack = []

        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)

    def backspaceCompareBruteForce(self, s: str, t: str) -> bool:
        return self._removeBackspacesBruteForce(s) == self._removeBackspacesBruteForce(t)

    def backspaceCompare(self, s: str, t: str) -> bool: # Milano's version
        s_index = len(s) - 1
        t_index = len(t) - 1
        s_skip = 0
        t_skip = 0

        while s_index >= 0 or t_index >= 0:
            if s_index >= 0 and s[s_index] == '#':
                s_index -= 1
                s_skip += 1
            elif s_index >= 0 and s_skip > 0:
                s_index -= 1
                s_skip -= 1
            elif t_index >= 0 and t[t_index] == '#':
                t_index -= 1
                t_skip += 1
            elif t_index >= 0 and t_skip > 0:
                t_index -= 1
                t_skip -= 1
            elif (s_index >= 0) != (t_index >= 0):
                return False
            elif s[s_index] != t[t_index]:
                return False
            else:
                s_index -= 1
                t_index -= 1
        
        return True

    def backspaceCompareZip(self, s: str, t: str) -> bool: # just for reference, using zip_longest function
        def F(S):
            skip = 0

            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))

# Tests

# Solution.backspaceCompare = Solution.backspaceCompareBruteForce
# Solution.backspaceCompare = Solution.backspaceCompareZip

assert Solution().backspaceCompare(s = "", t = "") == True
assert Solution().backspaceCompare(s = "#", t = "a") == False
assert Solution().backspaceCompare(s = "ab#c", t = "ad#c") == True
assert Solution().backspaceCompare(s = "ab##", t = "c#d#") == True
assert Solution().backspaceCompare(s = "a##c", t = "#a#c") == True
assert Solution().backspaceCompare(s = "a#c", t = "b") == False

assert Solution().backspaceCompare(s = "abc#d", t = "acc#c") == False
assert Solution().backspaceCompare(s = "x#y#z#", t = "a#") == True
assert Solution().backspaceCompare(s = "ab#z", t = "az#z") == True
assert Solution().backspaceCompare(s = "a###b", t = "b") == True
assert Solution().backspaceCompare(s = "Ab#z", t = "ab#z") == False

assert Solution().backspaceCompare("xywrrmp", "xywrrmu#p") == True
assert Solution().backspaceCompare("bxo#j##tw", "bxj##tw") == True
