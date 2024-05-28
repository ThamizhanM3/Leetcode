class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in "".join(s.lower().split()) if i.isalpha() or i.isdigit()])
        return True if s == s[::-1] else False