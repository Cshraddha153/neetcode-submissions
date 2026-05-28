class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #   BFS
        res=[]
        island = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            q = deque()
            grid[r][c]="0"
            q.append((r,c))
            while q:
                row, col =q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]=="0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc]="0"

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    bfs(r,c)
                    island+=1
        return island



















        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r>=rows or c>=cols or r<0 or c<0 or grid[r][c]=="0":
                return 
            grid[r][c]="0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1) 
            dfs(r, c-1)

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    dfs(r, c)
                    ans +=1
        return ans
            



















