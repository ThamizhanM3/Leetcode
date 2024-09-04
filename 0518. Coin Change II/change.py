class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for i in coins:
            for j in range(len(dp)):
                if j-i >= 0:
                    dp[j] += dp[j-i] 
        return dp[-1]