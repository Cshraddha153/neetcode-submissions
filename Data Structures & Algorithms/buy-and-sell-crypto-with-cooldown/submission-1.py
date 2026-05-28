class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1_buy, dp1_sell = 0, 0  
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = dp_buy, dp_sell

        return dp1_buy




        # bottom up tc=O(N)   sc=O(n)
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]  

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)

        return dp[0][1]










        # top down tc=O(n)  sc=O(N)
        dp = {}
        def dfs(i, buying):
            if i>=len(prices):
                return 0 

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i+1, buying) # not doing anything

            if buying:  # we are ready to buy
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
                return dp[(i, buying)]
            else:  # we are selling
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
                return dp[(i, buying)]
        
        return dfs(0, True)











        # recursive  tc=O(2^n) sc=O(N)
        def dfs(i, buying):
            if i>=len(prices):
                return 0 
            cooldown = dfs(i+1, buying) # not doing anything
            if buying:  # we are ready to buy
                buy = dfs(i+1, not buying) - prices[i]
                return max(buy, cooldown)
            else:  # we are selling
                sell = dfs(i+2, not buying) + prices[i]
                return max(sell, cooldown)
        
        return dfs(0, True)




