class Solution:
    def reverse(self, x: int) -> int:
        a = str(abs(x))
        a = a[::-1]
        n = int(a)
        p = pow(2, 31)
        if n > (p-1) or n < (-1*p):
            return 0
        return n if x > 0 else -1*n