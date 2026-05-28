class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        Atlantic = set()
        res = []
        row = len(heights)
        col = len(heights[0])

        def dfs(r, c, visit, prevheight):
            if ((r,c) in visit or r<0 or c<0 or r==row or c==col or heights[r][c]<prevheight):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for c in range(col):
            dfs(0, c, pacific, heights[0][c])
            dfs(row-1, c, Atlantic, heights[row-1][c])
        
        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, col-1, Atlantic, heights[r][col-1])


        res = []
        for r in range(row):
            for c in range(col):
                if (r, c) in pacific and (r, c) in Atlantic:
                    res.append([r, c])
        return res
                

        























