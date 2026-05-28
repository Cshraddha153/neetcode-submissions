class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
                
            if i>=len(nums)-1:
                return True

            r=nums[i]
            for j in range(1, r+1):
                if dfs(i+j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        
        return dfs(0)





        # Tc=O(N^N)   sc=O(N)
        def dfs(i):
            if i>=len(nums)-1:
                return True

            r=nums[i]
            for j in range(1, r+1):
                if dfs(i+j):
                    return True
            return False
        
        return dfs(0)

