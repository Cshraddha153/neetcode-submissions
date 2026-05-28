class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], -prices[i] + dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][1], prices[i] + dp[i + 1][0])
        
        return dp[0][0] 



        def rec(i, bought, dp):
            if i==len(prices):
                return 0

            if (i, bought) in dp:
                return dp[(i, bought)]

            res = rec(i+1, bought, dp)
            if bought:
                res = max(res, prices[i] + rec(i+1, False, dp))
            else:
                res = max(res, -prices[i] + rec(i+1, True, dp))
            dp[(i, bought)] = res
            return res
        dp = {}    
        return rec(0, False, dp)



        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i]>prices[i-1]:
        #         profit += prices[i]-prices[i-1]
        # return profit

