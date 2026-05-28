class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # tc=O(n^3)  sc=O(n^2)
        nums = [1] + nums + [1]
        dp={}
        def dfs(l, r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins+=dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        return dfs(1, len(nums)-2)









        # Tc=O(n*2^n)   sc=O(n*2^n)
        nums = [1] + nums + [1]
        def dfs(nums):
            if len(nums)==2:
                return 0
            maxCoins=0
            for i in range(1, len(nums)-1):
                coins = nums[i-1]*nums[i]*nums[i+1]
                coins += dfs(nums[:i] + nums[i+1:])
                maxCoins = max(maxCoins, coins)
            return maxCoins
        return dfs(nums)