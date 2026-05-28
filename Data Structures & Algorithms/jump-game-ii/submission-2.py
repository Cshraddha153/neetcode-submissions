class Solution:
    def jump(self, nums: List[int]) -> int:
        # goal = len(nums)-1
        # res = 0
        # for i in range(len(nums)-2,-1,-1):
        #     if i + nums[i] >=goal:
        #         res+=1
        #         goal = i
        # return res

        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]

            if i==len(nums)-1:
                return 0
                
            r = nums[i] 
            res = float('inf')
            for j in range(1, r+1):
                if i+j < len(nums):
                    res = min(res, 1 + dfs(i+j))
                    dp[i] = res
            return res           
        return dfs(0)






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


