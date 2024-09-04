class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        n = len(s)
        x = sorted(p)
        i = 0
        o = []
        while i < n-m+1:
            if sorted(s[i:m+i]) == x:
                o.append(i)
            i += 1
        return o