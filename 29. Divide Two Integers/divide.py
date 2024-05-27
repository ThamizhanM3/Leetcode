class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = int(dividend / divisor)
        p = pow(2, 31)
        if n > p-1:
            return p-1
        if n < -1*p:
            return -1*p
        return n