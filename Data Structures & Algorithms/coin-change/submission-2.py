class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}  #dict
        def solve(amount):
            if amount == 0:
                return 0
            if amount in dp:
                    return dp[amount]

            res = 1e9
            for coin in coins:    
                if amount - coin >= 0:
                    res = min(res, 1 + solve(amount-coin))
            dp[amount] = res
            return res
            
        minCoins = solve(amount)
        return -1 if minCoins>=1e9 else minCoins