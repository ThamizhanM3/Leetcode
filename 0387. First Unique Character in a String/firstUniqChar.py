class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)
        for i, c in enumerate(s):
            if x[c] == 1:
                return i
        return -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1