class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)


        # rec + hashset  tle
        wordSet = set(wordDict)
        def dfs(i):
            if i==len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        return True
            return False
        return dfs(0)



        # bottom up approach   tc=O(n*m*t)
        # sc = O(N)
        dp = [False]*(len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1,-1):
            for word in wordDict:
                l = len(word)
                if i + l <= len(s) and s[i : i+l] == word:
                    if dp[i+l]:
                        dp[i] = True
                        break
        return dp[0]




        # flag = False
        # i=0
        # while i != len(s):
        #     if i>len(s):
        #         break
        #     char = s[i]
        #     for word in wordDict:
        #         l = len(word)
        #         if s[i : i+l]==word:
        #             flag = True
        #             i = i+l
        #             break
                
        # return flag 
