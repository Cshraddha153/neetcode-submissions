class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total+nums[i]] += count 
                dp[i+1][total-nums[i]] += count
        return dp[n][target]
        
        
        
        # # tc=O(2^n)  sc=O(N)
        # def dfs(i, curr_sum):
        #     if i==len(nums):
        #         return curr_sum==target
        #     return dfs(i+1, curr_sum+nums[i]) + dfs(i+1, curr_sum-nums[i])
        # return dfs(0, 0)
