class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        o = s[0]
        c = len(o)
        for i in s[1:]:
            if i in o:
                o = o[o.index(i)+1:]
                o += i
            else:
                o += i
                c = max(c, len(o))
        return c