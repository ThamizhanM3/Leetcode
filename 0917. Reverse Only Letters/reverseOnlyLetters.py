class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a = []
        for i in s:
            if i.isalpha():
                a.append(i)
        a = a[::-1]
        o = ""
        for i in s:
            if i.isalpha():
                o += a.pop(0)
            else:
                o += i
        return o