class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #  dfs      tc=O(n^4)     sc=O(n^2)
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        minH = maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
            minH = min(minH, min(grid[row]))

        def dfs(node, t):
            r, c = node
            if (min(r, c) < 0 or max(r, c) >= n or 
                visit[r][c] or grid[r][c] > t):
                return False
            if r == (n - 1) and c == (n - 1):
                return True
            visit[r][c] = True
            return (dfs((r + 1, c), t) or
                    dfs((r - 1, c), t) or
                    dfs((r, c + 1), t) or
                    dfs((r, c - 1), t))

        for t in range(minH, maxH):
            if dfs((0, 0), t):
                return t
            for r in range(n):
                for c in range(n):
                    visit[r][c] = False
        
        return maxH





        # tc=O(4^n^2)    sc=O(N^2)
        # visited=set()
        # def dfs(r, c, maxheight):
        #     if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in visited:
        #         return 100000000
        #     if r==len(grid)-1 and c==len(grid[0])-1:
        #         return max(grid[r][c], maxheight)

        #     visited.add((r,c))
        #     maxheight = max(grid[r][c], maxheight)
        #     res = min(dfs(r+1, c, maxheight), dfs(r, c+1, maxheight) , dfs(r-1, c, maxheight) , dfs(r, c-1, maxheight))
        #     visited.remove((r,c))
        #     return res
            
        # return dfs(0, 0, 0)