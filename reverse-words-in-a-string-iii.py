# https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        
        for i in range(len(words)):
            words[i] = words[i][::-1]
        
        return ' '.join(words)

Solution().reverseWords(s = "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
Solution().reverseWords(s = "God Ding") == "doG gniD"
