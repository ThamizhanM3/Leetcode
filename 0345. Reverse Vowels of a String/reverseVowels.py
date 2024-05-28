class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        a = []
        b = []
        for i in s:
            a.append(i) if i in v else b.append(i)
        a = a[::-1]
        o = ""
        for i in s:
            if i in v:
                o += a.pop(0)
            else:
                o += b.pop(0)
        return o