class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(m-1):
            newrow = [1]*n
            for j in range(n-2, -1, -1):
                newrow[j] = newrow[j+1]+row[j]
            row = newrow
        return row[0]


        # # tc=sc=O(M*n)=sc
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[m-1][n-1] = 1
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         dp[i][j] += dp[i+1][j] + dp[i][j+1]
        # return dp[0][0]

        # tc=O(2^(m+n)) sc=O(m+n)
        # dp = {}
        # def dfs(r, c):
        #     if (r, c) in dp:
        #         return dp[(r, c)]
        #     if r>=m or c>=n:
        #         return 0
        #     if r==m-1 and c==n-1:
        #         return 1
        #     dp[(r, c)] = dfs(r+1, c)+dfs(r, c+1)
        #     return dp[(r, c)]
        # return dfs(0, 0)