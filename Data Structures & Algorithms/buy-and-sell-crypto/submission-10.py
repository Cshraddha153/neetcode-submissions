class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        ans = 0
        for r in range(1, len(prices)):
            p = prices[r]-prices[l]
            if prices[r]>prices[l]:
                ans = max(ans, p)
            else:
                l = r
        return ans




        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         res = max(res, profit)
        # return res