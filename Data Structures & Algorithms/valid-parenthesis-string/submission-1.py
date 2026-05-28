class Solution:
    def checkValidString(self, s: str) -> bool:
        # top down tc=O(N)  sc=O(N)
        dp = {}
        def dfs(i, open):
            if (i, open) in dp:
                return dp[(i, open)]
            if open<0:
                return False
            if i==len(s):
                return open==0
            if s[i]=="(":
                res = dfs(i+1, open+1)
            elif s[i]==")":
                res = dfs(i+1, open-1)
            else:
                res = (dfs(i+1, open) or dfs(i+1, open+1) or dfs(i+1, open-1))
            
            dp[(i, open)] = res
            return res
            
        return dfs(0,0)



        # recursive tc=O(3^n)  sc=O(N)
        def dfs(i, open):
            if open<0:
                return False
            if i==len(s):
                return open==0
            if s[i]=="(":
                return dfs(i+1, open+1)
            elif s[i]==")":
                return dfs(i+1, open-1)
            else:
                return (dfs(i+1, open) or dfs(i+1, open+1) or dfs(i+1, open-1))
        return dfs(0,0)




















        # TC=O(N)   sc=O(1)
        leftmin, leftmax = 0, 0
        for c in s:
            if c=="(":
                leftmin, leftmax = leftmin + 1, leftmax+1
            elif c==")":
                leftmin, leftmax = leftmin-1, leftmax-1
            else:
                leftmin, leftmax = leftmin-1, leftmax+1
            
            if leftmin<0:
                leftmin=0
            if leftmax<0:
                return False
        return leftmin==0

