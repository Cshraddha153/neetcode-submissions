class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh=0
        q=deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        
        time=0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q and fresh>0:
            n=len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row, col))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1

