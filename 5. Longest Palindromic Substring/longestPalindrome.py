class Solution:
    def isPalindrome(self, s):
        if s == s[::-1]:
            return s
        else:
            return ""
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxim = ""
        for i in range(n):
            for j in range(i, n):
                pal = self.isPalindrome(s[i:j+1])
                if len(pal) > len(maxim):
                    maxim = pal
            if len(maxim) > len(s)/2:
                return maxim
        return maxim


class Solution:
    def isPalindrome(self, s):
        if s == s[::-1]:
            return s
        else:
            return ""
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxim = ""
        for i in range(n):
            for j in range(i, n):
                pal = self.isPalindrome(s[i:j+1])
                if len(pal) > len(maxim):
                    maxim = pal
        return maxim