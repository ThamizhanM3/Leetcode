class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 0
        for i in range(1, 7):
            m = n//pow(5, i)
            if m == 0:
                break
            x += m
        return x



class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 0
        for i in range(1, 7):
            x += n//pow(5, i)
        return x