class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))
        i = 0
        if c == 1:
            return True
        while i <= n:
            x = (i*i) + (n*n)
            if x > c:
                n -= 1
            elif x < c:
                i += 1
            else:
                return True
        return False