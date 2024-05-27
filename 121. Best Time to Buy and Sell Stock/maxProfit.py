class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # x = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if x < prices[j]-prices[i]:
        #             x = prices[j]-prices[i]
        # return x
        lsf = prices[0]
        pist = 0
        op = 0
        for i in prices[1:]:
            if lsf > i:
                lsf = i
            pist = i-lsf
            op = max(op, pist)
        return op
        #return abs(min(prices) - max(prices[prices.index(min(prices)):]))