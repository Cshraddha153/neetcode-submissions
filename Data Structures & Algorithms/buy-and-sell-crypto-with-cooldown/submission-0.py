class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # top down tc=O(n)  sc=O(N)
        # dp = {}
        # def dfs(i, buying):
        #     if i>=len(prices):
        #         return 0 

        #     if (i, buying) in dp:
        #         return dp[(i, buying)]

        #     cooldown = dfs(i+1, buying) # not doing anything
        #     if buying:  # we are ready to buy
        #         buy = dfs(i+1, not buying) - prices[i]
        #         return max(buy, cooldown)
        #     else:  # we are selling
        #         sell = dfs(i+2, not buying) + prices[i]
        #         return max(sell, cooldown)
        
        # return dfs(0, True)











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




