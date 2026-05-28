class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        dp[n] = nextDp[n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                nextDp[j] = dp[j]
                if s[i] == t[j]:
                    nextDp[j] += dp[j + 1]
            dp = nextDp[:]

        return dp[0]
        # Bottom-Up
        # tc=O(m*n)  sc=O(m*N)
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i]==t[j]:
                    dp[i][j]+=dp[i+1][j+1]
        return dp[0][0]


















        # top down  tc=O(m*n)  sc=O(m*N)
        dp = {}
        if len(s)<len(t):
            return 0
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i,j)]

            if j==len(t):
                return 1
            if i==len(s):
                return 0
            dp[(i,j)] = dfs(i+1, j)
            
            if s[i]==t[j]:
                dp[(i,j)]+=dfs(i+1, j+1)
                
            return dp[(i,j)]

        return dfs(0, 0)











        # tc = O(2^m)   sc=O(m)
        if len(s)<len(t):
            return 0
        def dfs(i, j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            res = dfs(i+1, j)
            print("res", res, "i=",i, "j=",j)
            if s[i]==t[j]:
                res+=dfs(i+1, j+1)
                print("res in s[i] and t[j]", res, "i=",i, "j=",j)
            return res

        return dfs(0, 0)
