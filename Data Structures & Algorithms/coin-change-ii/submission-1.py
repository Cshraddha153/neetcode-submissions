class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down + memoization
        memo = {}
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if total==amount:
                return 1
            if total>amount or i>len(coins)-1:
                return 0

            include = dfs(i, total + coins[i])
            exclude = dfs(i+1, total)
            memo[(i, total)] = include + exclude
            return memo[(i, total)]
        
        
        return dfs(0, 0)

        # we need to find the combinations thats why incl nd exclu increase krna pagega
        # def dfs(i, total):
        #     if total==amount:
        #         return 1
        #     if total>amount or i>len(coins)-1:
        #         return 0

        #     include = dfs(i, total + coins[i])
        #     exclude = dfs(i+1, total)
        #     return include + exclude
        
        
        # return dfs(0, 0)