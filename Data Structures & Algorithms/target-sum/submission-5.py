class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr_sum):
            if i==len(nums):
                return curr_sum==target
            return dfs(i+1, curr_sum+nums[i]) + dfs(i+1, curr_sum-nums[i])
        
        return dfs(0, 0)
