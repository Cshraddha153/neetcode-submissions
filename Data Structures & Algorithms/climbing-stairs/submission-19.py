class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        for i in range(n):
            temp=two
            two = one+two
            one=temp
            print(one, two)
        return two




        if n<3:
            return n
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]



        # top down tc=O(n)=sc
        memo = [-1]*(n+1)
        def dfs(i):
            if i==1:
                return 1
            if i==2:
                return 2 
            if memo[i]!=-1:
                return memo[i]
            memo[i] = dfs(i-1) + dfs(i-2)
            return memo[i]
        return dfs(n)





       # recursive soln
        def dfs(i):
            if i==1:
                return 1
            if i==2:
                return 2 
            return dfs(i-1) + dfs(i-2)

        return dfs(n)