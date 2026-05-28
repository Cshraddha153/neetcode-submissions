class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        row, col = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if r>=row or c>=col or (r, c) in visited or r<0 or c<0 or grid[r][c]==0:
                return 0
            visited.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    temp = dfs(r, c)
                    area = max(area, temp)
        return area
            
            
