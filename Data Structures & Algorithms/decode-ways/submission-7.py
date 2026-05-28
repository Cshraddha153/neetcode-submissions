class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s)-1, -1, -1):
            if s[i]=="0":
                dp = 0
            else:
                dp =dp1
            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                dp+=dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1













        # bottom up approach
        dp = {len(s):1}
        for i in range(len(s)-1, -1, -1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i] = dp[i+1]
            if i+1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                dp[i]+=dp[i+2]
        return dp[0]

















        # top down approach tc=O(N)  sc=O(N)
        map1 = {len(s):1}
        def dfs(i):
            if i in map1:
                return map1[i]
            if s[i]=="0":
                return 0
            res = dfs(i+1)
            if i<len(s)-1:
                if (s[i]=="1" or s[i]=="2" and s[i+1]< "7"):
                    res += dfs(i+2)
            map1[i] = res
            return res
        return dfs(0)











        # recursive tc=2^n   sc=O(n)
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i]=="0":
        #         return 0
        #     res = dfs(i+1)
        #     if i<len(s)-1:
        #         if (s[i]=="1" or s[i]=="2" and s[i+1]< "7"):
        #             res += dfs(i+2)
        #     return res
        # return dfs(0)