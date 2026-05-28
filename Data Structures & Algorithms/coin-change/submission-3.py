class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming (Bottom-Up)
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1 




























        # Dynamic Programming (Top-Down)
        # dp = {}  #dict
        # def solve(amount):
        #     if amount == 0:
        #         return 0
        #     if amount in dp:
        #             return dp[amount]

        #     res = 1e9
        #     for coin in coins:    
        #         if amount - coin >= 0:
        #             res = min(res, 1 + solve(amount-coin))
        #     dp[amount] = res
        #     return res
            
        # minCoins = solve(amount)
        # return -1 if minCoins>=1e9 else minCoins

        # TC---> O(n*t) n->coin array length t->amount
        # SC---> )(t)









