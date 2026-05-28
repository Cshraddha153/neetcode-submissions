class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posdiag = set()
        negdiag = set()
        col = set()
        res = []
        grid = [["." for r in range(n)] for c in range(n)]
        print(grid)

        def dfs(r):
            if r==n:
                copy = ["".join(row) for row in grid]
                return res.append(copy)

            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue

                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                grid[r][c]="Q"

                dfs(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                grid[r][c] = "."

        dfs(0)
        return res
