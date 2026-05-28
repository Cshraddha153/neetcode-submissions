class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy   tc=O(n)   sc=O(1)
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i]>=goal:
                goal=i
        return goal==0






        # tc=O(N^2)  sc=O(n)  Bottom up

        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n-2, -1, -1):
            end = min(n, i+nums[i]+1)
            for j in range(i+1, end):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]





















        # tc=O(N^2)  sc=O(n)  top down
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

