class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, total):
            if i==len(nums):
                return 1 if total == target else 0
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            return pos + neg

        return dfs(0, 0)