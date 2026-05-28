class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n  # 1,1,1,1,1,1,1    # 7,6,5,4,3,2,1 
        for i in range(m-1):
            newRow = [1]*n  #1,
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]  # 7,6,5,4,3,2,1   # 28,21,15,10,6,3,1
            row = newRow  # 7,6,5,4,3,2,1  # 28,21,15,10,6,3,1
        return row[0]  # 28