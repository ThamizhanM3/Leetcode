class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x = ''
        y = ''
        for i in s:
            if i == '#':
                if len(x):
                    x = x[:-1]
            else:
                x += i
        for i in t:
            if i == '#':
                if len(y):
                    y = y[:-1]
            else:
                y += i

        return x == y