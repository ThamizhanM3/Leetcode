class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        i = 0
        j = 1
        for x in range(n-1):
            i, j = j, i+j
        return j



class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)



class Solution:
    def fib(self, n: int) -> int:
        a = []
        a.append(0)
        a.append(1)
        for i in range(2, n+1):
            a.append(a[i-1] + a[i-2])
        return a[n]