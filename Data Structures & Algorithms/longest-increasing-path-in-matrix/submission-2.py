class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # topoloical sort  O(N*M)  sc&tc
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        indegree = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                for d in directions:
                    nr, nc = d[0] + r, d[1] + c
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        matrix[nr][nc] < matrix[r][c]
                    ):
                        indegree[r][c] += 1

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    q.append([r, c])

        LIS = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        matrix[nr][nc] > matrix[r][c]
                    ):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append([nr, nc])
            LIS += 1
        return LIS











        # tc=O(m*N)   sc=O(M*N)
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