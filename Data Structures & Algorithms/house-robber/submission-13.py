class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom-Up
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]



























        # Top-Down  tc=O(n)  sc=O(n)
        memo = [-1]*len(nums)
        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            return memo[i]
        return dfs(0)



        # Recursion
        def dfs(i):
            if i>=len(nums):
                return 0
            
            return max(dfs(i+1), nums[i]+ dfs(i+2))
        return dfs(0)



        # Space Optimized)
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            temp = max(rob2, rob1+nums[i])
            rob1 = rob2
            rob2 = temp
        return rob2 