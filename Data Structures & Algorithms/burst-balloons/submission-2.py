class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l>r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        
        return dfs(1, len(nums)-2)






        # def dfs(nums):
        #     if len(nums)==2:
        #         return 0
        #     max_coins = 0
        #     for i in range(1, len(nums)-1):
        #         coins = nums[i-1]*nums[i]*nums[i+1]
        #         coins+=dfs(nums[:i] + nums[i+1:])
        #         max_coins = max(max_coins, coins)
        #     return max_coins
        
        # return dfs(nums)