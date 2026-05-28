class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        visit = set()
        q=deque()
        def multisourcebfs(r, c):
            if r>=row or c>=col or grid[r][c] == -1 or r<0 or c<0 or (r, c) in visit:
                return
            visit.add((r, c))
            q.append([r, c])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append([r, c])
                    visit.add((r,c))
       
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                multisourcebfs(r+1, c)
                multisourcebfs(r-1, c)
                multisourcebfs(r, c+1)
                multisourcebfs(r, c-1)
            dist+=1
        
            
        