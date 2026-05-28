class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        
        while m-1:
            print(m-1)
            temp = [1]*n
            for i in range(n):
                temp[n-2-i] = row[n-2-i] + temp[n-i-1]
            row=temp
            print(row)
            m-=1
        return row[0]
                