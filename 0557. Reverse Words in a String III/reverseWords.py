class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        b = []
        for i in a:
            b.append(i[::-1])
        return " ".join(b)