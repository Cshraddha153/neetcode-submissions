class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        def dfs(i):
            if i>=len(nums):
                return 0
            return nums[i] + min(dfs(i+1), dfs(i+2))

        return min(dfs(0), dfs(1))
