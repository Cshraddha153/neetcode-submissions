class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        
        def solve(i):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]

            dp[i] = max(nums[i]+solve(i+2), solve(i+1))
            return dp[i]

        return solve(0)