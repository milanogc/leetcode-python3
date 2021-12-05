class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif not stack or pairs[c] != stack.pop():
                return False
        
        return not stack

# Tests

assert Solution().isValid(s = "()")
assert Solution().isValid(s = "()[]{}")
assert not Solution().isValid(s = "(]")
assert not Solution().isValid(s = "([)]")
assert Solution().isValid(s = "{[]}")
