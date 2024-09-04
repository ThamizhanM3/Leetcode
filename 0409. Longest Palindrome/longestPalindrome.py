class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = Counter(s)
        s = 0
        o = 0
        op = 0
        tot = 0
        for i in x.items():
            tot += i[1]
            if i[1] % 2 == 0:
                s += i[1]
            else:
                op = 1
                o += i[1]-1
        return s+o+1 if op else s