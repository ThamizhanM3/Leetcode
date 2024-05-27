class Solution:
    def fun(self, n, arr):
        if n < 0:
            return 0
        if arr[n] != -1:
            return arr[n]
        if n == 1 or n == 0:
            return 1
        arr[n] = self.fun(n-1, arr) + self.fun(n-2, arr)
        return arr[n]

    def climbStairs(self, n: int) -> int:
        arr = [-1 for i in range(n+1)]
        return self.fun(n, arr)