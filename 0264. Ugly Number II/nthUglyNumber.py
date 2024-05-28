class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        while len(dp) < n:
            v2 = 2*dp[p2]
            v3 = 3*dp[p3]
            v5 = 5*dp[p5]
            if v2 <= v3 and v2 <= v5:
                if dp[-1] != v2:
                    dp.append(v2)
                p2 += 1
            elif v3 <= v2 and v3 <= v5:
                if dp[-1] != v3:
                    dp.append(v3)
                p3 += 1
            elif v5 <= v2 and v5 <= v3:
                if dp[-1] != v5:
                    dp.append(v5)
                p5 += 1
        return dp[-1]