class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #   BFS
        res=[]
        island = 0
        def bfs(r, c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=="0":
                return
            q = deque()
            q.append((r,c))
            while q:
                row, col =q.popleft()
                grid[row][col]="0"
                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r, c-1)

        
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
            



















