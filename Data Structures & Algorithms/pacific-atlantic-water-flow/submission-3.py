class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS
        # we can do two dfs
        # for pacific ocean--> top + left
        # for atlantic ocean--> right+ bottom

        # ans--> those cells which can reach pac+ atlantic ocean
        # tc=O(M*N)=sc
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if (r, c) in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c]<prev_height:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) #top row pac
            dfs(rows-1, c, atl, heights[rows-1][c]) #bottom atl
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # left col pacific ocean
            dfs(r, cols-1, atl, heights[r][cols-1]) # right atlanatic ocean
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append((r, c))
        return res
