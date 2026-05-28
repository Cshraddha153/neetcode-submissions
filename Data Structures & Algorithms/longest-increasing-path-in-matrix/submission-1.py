class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        memo = {} 
        def dfs(r, c, prev):
            if r<0 or c<0 or r>=row or c>=col or matrix[r][c]<=prev:
                return 0

            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 1 + max(dfs(r+1, c, matrix[r][c]), dfs(r-1, c, matrix[r][c]), dfs(r, c+1, matrix[r][c]), dfs(r, c-1, matrix[r][c]))
            memo[(r, c)] = res
            return res
        
        ans=0
        for r in range(row):
            for c in range(col):
                ans = max(ans, dfs(r,c, float("-inf")))
        return ans