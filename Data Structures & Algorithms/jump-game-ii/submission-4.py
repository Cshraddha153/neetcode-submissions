class Solution:
    def jump(self, nums: List[int]) -> int:
        # bottom up  tc=O(N^2)  sc=O(N)
        # n = len(nums)
        # dp = [1000000] * n
        # dp[-1] = 0

        # for i in range(n - 2, -1, -1):
        #     end = min(n, i + nums[i] + 1)
        #     for j in range(i + 1, end):
        #         dp[i] = min(dp[i], 1 + dp[j])
        # return dp[0]


        # tc=O(N)  sc=O(1)  greedy
        l=0
        r=0
        res=0
        while r<len(nums)-1:
            farthest=0
            for i in range(l, r+1):
                farthest=max(farthest, nums[i]+i)
            l = r+1
            r = farthest
            res+=1
        return res



        # tc = O(N^2)  sc=O(N)
        # dp = {}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]

        #     if i==len(nums)-1:
        #         return 0

        #     r = nums[i] 
        #     res = float('inf')
        #     for j in range(1, r+1):
        #         if i+j < len(nums):
        #             res = min(res, 1 + dfs(i+j))
        #             dp[i] = res
        #     return res           
        # return dfs(0)






        # tc=O(N^N)  sc=O(N)   Recursive
        def dfs(i):
            if i==len(nums)-1:
                return 0
            r = nums[i] 
            res = float('inf')
            for j in range(1, r+1):
                if i+j < len(nums):
                    res = min(res, 1 + dfs(i+j))
            return res           
        return dfs(0)


