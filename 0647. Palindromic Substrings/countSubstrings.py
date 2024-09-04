class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        sp = 0
        n = len(s)
        for sp in range(n):
            i = 0
            j = i + sp
            while j < n:
                a = s[i:j+1]
                if a == a[::-1]:
                    c += 1
                j += 1
                i += 1
        return c