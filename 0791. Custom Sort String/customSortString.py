class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = [i for i in s]
        opt = ''
        for i in order:
            opt += i*s.count(i)
        for i in s:
            if i not in order:
                opt += i
        return opt