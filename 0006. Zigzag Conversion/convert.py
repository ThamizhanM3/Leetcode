class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        dg = numRows-2 if numRows > 1 else 0
        ln = numRows-1 if numRows > 0 else 0
        if numRows == 1:
            return s
        opt = ''
        i = 0
        while i < n:
            opt += s[i]
            i += dg + ln + 1
        for k in range(1, dg+1):
            i = 0
            while i < n+dg:
                if i-k > 0 and i-k < n:
                    opt += s[i-k]
                if i+k < n and i+k > 0:
                    opt += s[i+k]
                i += dg + ln + 1
        i = 0
        while i < n:
            if i+ln < n:
                opt += s[i+ln]
            i += dg + ln + 1
        return opt