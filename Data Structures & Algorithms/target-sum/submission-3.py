class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # MEMOIZATION
        memo = {}
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if i==len(nums):
                return 1 if total == target else 0
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            memo[(i, total)] = pos + neg
            return memo[(i, total)]

        return dfs(0, 0)


        # RECURSION
        def dfs(i, total):
            if i==len(nums):
                return 1 if total == target else 0
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            return pos + neg

        return dfs(0, 0)