class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs  tc=sc=O(m*n)
        fresh = 0
        rotten = 0
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    rotten+=1
                    q.append((r, c))
                else:
                    continue
        time = 0
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if (r+dr in range(len(grid))) and (c+dc in range(len(grid[0]))) and grid[r+dr][c+dc]==1:
                        
                        grid[r+dr][c+dc]=2
                        fresh-=1
                        q.append((r+dr, c+dc))
            time+=1
        return time if fresh==0 else -1
        

