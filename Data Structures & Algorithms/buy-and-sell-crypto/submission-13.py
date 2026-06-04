class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # tc=O(n2)  sc=O(1) ---> Brute Force
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                res = max(res, sell-buy)
        return res




        # Two pointer
        # max_profit = 0
        # l = 0 # buy at lowest
        # # r-->sell at highest
        # for r in range(len(prices)):
        #     if prices[l]>prices[r]:
        #         l = r
        #     max_profit = max(max_profit, prices[r]-prices[l])
        # return max_profit 