class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        hold = prices[0]
        total = 0
        while i < len(prices):
            print(hold, prices[i])
            if hold > prices[i]:
                if prices[i] - hold > 0:
                    total += prices[i] - hold
                hold = prices[i]
            else:
                total += prices[i] - hold
                hold = prices[i]
            i += 1
        return total