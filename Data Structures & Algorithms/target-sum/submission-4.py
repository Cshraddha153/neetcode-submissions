class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
            
        return dp[target]





        # MEMOIZATION  tc=O(n*m)   sc=O(N*M)
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


        # RECURSION  TC=2^N   SC=O(n)
        def dfs(i, total):
            if i==len(nums):
                return 1 if total == target else 0
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            return pos + neg

        return dfs(0, 0)