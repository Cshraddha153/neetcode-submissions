class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down   tc=O(m*n)   sc=O(m*n)
        memo = [[-1]*n for i in range(m)]
        print(memo)
        def dfs(i, j):
            if i==(m-1) and j==(n-1):
                return 1
            if i>m-1 or j>n-1:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i, j+1) + dfs(i+1, j)

            return memo[i][j]

        return dfs(0, 0)






















        # Recursion
        # def dfs(i, j):
        #     if i==(m-1) and j==(n-1):
        #         # print("call")
        #         return 1
        #     if i>=m or j>=n:
        #         return 0
        #     return dfs(i, j+1) + dfs(i+1, j)
        # return dfs(0,0)























        # Space Optimized  tc=O(m*n)   sc=O(n)
        # row = [1]*n
        # while m-1:
        #     temp = [1]*n
        #     for i in range(n):
        #         temp[n-2-i] = row[n-2-i] + temp[n-i-1]
        #     row=temp
        #     m-=1
        # return row[0]
                