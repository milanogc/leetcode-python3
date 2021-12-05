# https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(' ')
        
        for i in range(len(t)):
            t[i] = t[i][::-1]
        
        return ' '.join(t)

Solution().reverseWords(s = "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
Solution().reverseWords(s = "God Ding") == "doG gniD"
