class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # space optimized 
        n = len(nums)
        dp = [float("inf")]*(n+1)
        dp[n] = 0

        for m in range(1, k+1):
            nextDp = [float("inf")]*(n+1)
            for i in range(n-1, -1, -1):
                curSum=0
                for j in range(i, n-m+1):
                    curSum += nums[j]
                    nextDp[i] = min(nextDp[i], max(curSum, dp[j+1]))
            dp = nextDp
        return dp[0]


        # top down
        # n = len(nums)
        # dp = [[float("inf")]*(k+1) for _ in range(n+1)]
        # dp[n][0] = 0

        # for m in range(1, k+1):
        #     for i in range(n-1, -1, -1):
        #         curSum = 0
        #         for j in range(i, n-m+1):
        #             curSum += nums[j]
        #             dp[i][m] = min(dp[i][m], max(curSum, dp[j+1][m-1]))
        # return dp[0][k]

        # recursion + top down
        # n = len(nums)
        # def dfs(i, m, dp):
        #     if i==n:
        #         return 0 if m == 0 else float("inf")
        #     if m==0:
        #         return float("inf")
        #     if (i, m) in dp:
        #         return dp[(i, m)]
        #     res = float("inf")
        #     curSum = 0
        #     for j in range(i, n-m+1):
        #         curSum += nums[j]
        #         res = min(res, max(curSum, dfs(j+1, m-1, dp)))
        #     dp[(i, m)] = res
        #     return res

        # dp = {}
        # return dfs(0, k, dp)



        # binary search
        # def canSplit(largest):
        #     subarray = 1
        #     curSum=0
        #     for num in nums:
        #         curSum += num
        #         if curSum > largest:
        #             subarray += 1
        #             if subarray > k:
        #                 return False
        #             curSum = num
        #     return True
        
        # l, r =  max(nums), sum(nums)
        # res = r
        # while l<=r:
        #     mid = l + (r-l)//2
        #     if canSplit(mid):
        #         res = mid
        #         r = mid-1
        #     else:
        #         l=mid+1
        # return res
        
