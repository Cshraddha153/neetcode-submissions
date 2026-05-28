class Solution:
    def climbStairs(self, n: int) -> int:
        # memoization   o(n)-tc, O(n)-sc
        # dp = [-1]*(n+1)
        # def solve(i):
        #     if i==0:
        #         return 1
        #     if i==1:
        #         return 1
        #     if dp[i]!=-1:
        #         return dp[i]
        #     if i>=2:
        #         dp[i] = solve(i-1) + solve(i-2)
        #         return dp[i]

        # return solve(n)

        #Bottom up approach
        #base case
        # if n<=2:
        #     return n

        # dp=[0]*(n+1)
        # dp[1]=1
        # dp[2]=2     
        # for i in range(3, n+1): 
        #     dp[i] = dp[i-1] + dp[i-2] 
        # return dp[n]


        # Space Optimized
        # if n<=2:
        #     return n
        one=1
        two=1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one











