class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)





        # tc=O(N^2)  sc=O(n)
        n = len(nums)
        memo = [-1] * n
        def dfs(i):
            if memo[i]!=-1:
                return memo[i]
            
            LIS = 1
            for j in range(i+1, n):
                if nums[i]<nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            memo[i] = LIS
            return LIS
        
        return max(dfs(i) for i in range(n))
            




        # Top-Down  tc = sc =O(N^2)
        dp = [[-1]*(len(nums)+1) for _ in range(len(nums)+1)]
        # print("dp", dp)
        def dfs(i, j):
            if i==len(nums):
                return 0
            if dp[i][j+1]!=-1:
                return dp[i][j+1]

            LIS = dfs(i+1, j) # not include
            
            if j==-1 or nums[j]<nums[i]:
                LIS = max(LIS, 1 + dfs(i+1, i)) #include

            dp[i][j+1] = LIS
            return LIS
        
        return dfs(0, -1)



        # recursive
        def dfs(i, j):
            if i==len(nums):
                return 0

            LIS = dfs(i+1, j) # not include

            if j==-1 or nums[j]<nums[i]:
                LIS = max(LIS, 1 + dfs(i+1, i))
            return LIS

        return dfs(0, -1)

        # ans=0
        # for i in range(len(nums)-1, -1, -1):
        #     length=1
        #     ele = nums[i]
        #     print("ele", ele)
        #     for j in range(i-1, -1, -1):
        #         if nums[j]<ele:
        #             print("nums[j]", nums[j], j)
        #             length+=1
        #             ele = nums[j]
        #             print(ele)
        #     ans = max(ans, length)
        # return ans