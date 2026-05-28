class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        if len(s)<len(t):
            return 0
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i,j)]

            if j==len(t):
                return 1
            if i==len(s):
                return 0
            dp[(i,j)] = dfs(i+1, j)
            
            if s[i]==t[j]:
                dp[(i,j)]+=dfs(i+1, j+1)
                
            return dp[(i,j)]

        return dfs(0, 0)











        # tc = O(2^m)   sc=O(m)
        if len(s)<len(t):
            return 0
        def dfs(i, j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            res = dfs(i+1, j)
            print("res", res, "i=",i, "j=",j)
            if s[i]==t[j]:
                res+=dfs(i+1, j+1)
                print("res in s[i] and t[j]", res, "i=",i, "j=",j)
            return res

        return dfs(0, 0)
